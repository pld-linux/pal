# TODO:
#  - handle with i18n files
#
Summary:	A command line calendar that displays holidays and user-defined events.
Name:		pal
Version:	0.3.4
Release:	0.1
License:	GPL v2
Group:		Applications/Text
URL:		http://palcal.sourceforge.net/
Source0:	http://dl.sf.net/palcal/%{name}-%{version}.tgz
# Source0-md5:	86911792eace630a1c2e93846c27290c
Patch0:		%{name}-home_etc.patch
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pal is a command line calendar that displays holidays and user-defined
events that are specified in text files. Recomended:
 - LaTex - required for creating ps/pdf/dvi claendars.
 - at, cron, sendmail - required for event reminders via email

%define debug_package %{nil}

%prep
%setup -q
%patch0 -p1

%build
sed 's/VERSION/%{version}/' pal.1.template > pal.1
cd src
%{__make}

cd ../po
for file in *po; do
	f=`echo $file|cut -f1 -d.`
	mkdir -p "$f/LC_MESSAGES"
	msgfmt $file -o "$f/LC_MESSAGES/%{name}.po"
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

install src/pal $RPM_BUILD_ROOT%{_bindir}
install share/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install pal.conf $RPM_BUILD_ROOT%{_sysconfdir}
install pal.1 $RPM_BUILD_ROOT%{_mandir}/man1

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc ChangeLog doc/*
%{_mandir}/man1/*
%{_datadir}/pal
%{_sysconfdir}/pal.conf
