Summary:	Arc archiver
Summary(pl.UTF-8):	Archiwizer arc
Name:		arc
Version:	5.21j
Release:	1
License:	distributable if unmodified
Group:		Applications/Archiving
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	b3c12bbc71c440df19d3a8a653d4baf5
Patch0:		%{name}-time.patch
Patch1:		%{name}-gcc4.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%description -l pl.UTF-8
arc jest archiwizerem i kompresorem plików. Dawno zastąpiony przez
parę zip/unzip, ale nadal przydatny jeżeli potrzebujesz rozpakować
stare archiwa .arc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%doc Arc521.doc Arcinfo Changes.521 Readme
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/arc.1*
