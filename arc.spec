Summary:	Arc archiver
Summary(pl.UTF-8):	Archiwizer arc
Name:		arc
Version:	5.21p
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://downloads.sourceforge.net/arc/%{name}-%{version}.tar.gz
# Source0-md5:	902ce24b23422880d474df6f1d9eba5e
Patch0:		%{name}-time.patch
URL:		http://arc.sourceforge.net/
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

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install arc marc $RPM_BUILD_ROOT%{_bindir}

install arc.1 marc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Arc521.doc Arcinfo Changelog LICENSE Readme
%attr(755,root,root) %{_bindir}/arc
%attr(755,root,root) %{_bindir}/marc
%{_mandir}/man1/arc.1*
%{_mandir}/man1/marc.1*
