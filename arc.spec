Summary:	Arc archiver
Summary(pl):	Archiwizer arc
Name:		arc
Version:	5.21e
Release:	6
License:	distributable if unmodified
Group:		Applications/Archiving
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}521e.pl8.tar.Z
# Source0-md5:	a6eca0eb9d8cfb8d9bb62753c85759cb
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
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install arc marc $RPM_BUILD_ROOT%{_bindir}

install arc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Arc521.doc Arcinfo Changes.521 README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/arc.1*
