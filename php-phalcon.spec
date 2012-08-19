Name:           php-phalcon
Version:        0.4.4
Release:        1%{?dist}
Summary:        PhalconPHP is a web framework delivered as a C extension 

License:        BSD
URL:            http://phalconphp.com
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc php-devel php-mysql php-pear
Requires:       php-mysql php-pear
Requires:       php(zend-abi) >= 20090626 
Requires:       php(api) >= 20090626 

%description
PhalconPHP is a web framework delivered as a C extension 

%prep
%setup -q
cat > phalcon.ini << 'EOF'
; Enable phalcon extension module
extension = phalcon.so 
EOF

%build
cd release
CFLAGS="-O2 -fno-delete-null-pointer-checks"
phpize
%configure --enable-phalcon
make %{?_smp_mflags}


%install
rm -rf %{buildroot} 
pushd release
make install INSTALL_ROOT=%{buildroot}
popd
%{__install} -D -m 644 phalcon.ini %{buildroot}%{php_inidir}/phalcon.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{php_extdir}/phalcon.so
%config(noreplace) %{php_inidir}/phalcon.ini


%changelog
* Sat Aug 18 2012 Tavis Aitken <tavisto@tavisto.net> 0.4.4-1
- Initial build
