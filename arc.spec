Summary:	Arc archiver
Summary(pl):	Archiwizer arc
Name:		arc
Version:	5.21e
Release:	4
License:	Distributable if unmodified
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}521e.pl8.tar.Z
Patch0:		%{name}-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%description -l pl
arc jest archiwizerem i kompresorem plików. Dawno zast±piony przez
parê zip/unzip, ale nadal przydatny je¿eli potrzebujesz rozpakowaæ
stare archiwa .arc.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install arc marc $RPM_BUILD_ROOT%{_bindir}

install arc.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf Arc521.doc Arcinfo Changes.521 README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/arc.1*
%doc *.gz
