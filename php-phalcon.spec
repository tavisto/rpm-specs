Name:           phalcon-php
Version:        0.4.4
Release:        1%{?dist}
Summary:        PhalconPHP is a web framework delivered as a C extension 

License:        BSD
URL:            http://phalconphp.com/index  
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc php-devel php-mysql php-pear
Requires:       php-mysql php-pear

%description
PhalconPHP is a web framework delivered as a C extension 

%prep
%setup -q


%build
cd release
phpize
%configure --enable-phalcon
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd release
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog
* Sat Aug 18 2012 Tavis Aitken <tavisto@tavisto.net> 0.4.4-1
- Initial build
