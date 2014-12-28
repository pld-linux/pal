# TODO:
#  - handle with i18n files
#
Summary:	A command line calendar that displays holidays and user-defined events
Summary(pl.UTF-8):	Działający z linii poleceń kalendarz wyświetlający święta i inne zdarzenia
Name:		pal
Version:	0.3.4
Release:	0.1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/palcal/%{name}-%{version}.tgz
# Source0-md5:	86911792eace630a1c2e93846c27290c
Patch0:		%{name}-home_etc.patch
URL:		http://palcal.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.2
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pal is a command line calendar that displays holidays and user-defined
events that are specified in text files. Recomended:
 - LaTeX - required for creating ps/pdf/dvi calendars.
 - at, cron, some MTA - required for event reminders via email

%description -l pl.UTF-8
pal to działający z linii poleceń kalendarz wyświetlający święta i
zdarzenia zdefiniowane przez użytkownika podane w plikach tekstowych.
Zalecane:
 - LaTeX - wymagany do tworzenia kalendarzy ps/pdf/dvi.
 - at, cron, jakiś MTA - wymagane do wysyłania przypominajek
   pocztą elektroniczną.

%prep
%setup -q
%patch0 -p1

%build
sed 's/VERSION/%{version}/' pal.1.template > pal.1
%{__make} -C src

# ???
#cd po
#for file in *po; do
#	f=`echo $file|cut -f1 -d.`
#	mkdir -p "$f/LC_MESSAGES"
#	msgfmt $file -o "$f/LC_MESSAGES/%{name}.po"
#done

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
