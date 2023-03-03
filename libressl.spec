Summary: LibreSSL 3.6.2
Name: libressl
Version: %{?version}%{!?version:3.6.2}
Release: 1%{?dist}
Obsoletes: %{name} <= %{version}
Provides: %{name} = %{version}
URL: https://www.libressl.org/
License: GPLv2+

Source: https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{name}-%{version}.tar.gz

BuildRequires: make gcc perl 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%global openssldir /usr

%description
https://github.com/philyuchkoff/openssl-RPM-Builder
LibreSSL RPM for version 3.6.2

%package devel
Summary: Development files for programs which will use the openssl library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
LibreSSL RPM for version 3.6.2 (development package)

%prep
%setup -q

%build
./config --prefix=%{openssldir} --openssldir=%{openssldir}
make

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%make_install


%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%{openssldir}
%defattr(-,root,root)

%files devel
%{openssldir}/include/*
%defattr(-,root,root)

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
