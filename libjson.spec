Name:           libjson
Version:        0.2.0
Release:        1%{?dist}
Summary:        A MIT-licensed open source RFC 4627 compliant JSON library   

Group:          System Environment/Libraries
License:        MIT 
URL:            https://github.com/thanatos/libjson
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake

%description
A MIT-licensed open source RFC 4627 compliant JSON library

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc
/usr/lib/*.so

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
/usr/lib/*.so
/usr/lib/pkgconfig/*.pc


%changelog
* Sun Jun 26 2011 - Tavis Aitken <tavisto@tavisto.net> - 0.2.0-1
- Initial package.
