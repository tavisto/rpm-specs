%define php_name Symfony

Summary:    A PHP Web Development Framework
Name:       php-Symfony
Version:    2.0.4
Release:    1%{?dist}

License:    MIT
Group:      Development/Libraries

# wget https://github.com/symfony/symfony/tarball/v{version} -0 php-Symfony-{version}-raw.tar.gz
# tar -xzvf php-Symfony-{version}-raw.tar.gz
# tar -czvf v{version} php-Symfony-{version}.tar.gz

Source0:    %{php_name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:        http://symfony.com/

BuildArch:  noarch

Requires: php >= 5.3.2

%description
Symfony2 is a PHP 5.3 full-stack web framework.
It is written with speed and flexibility in mind.
It allows developers to build better and easy to maintain websites with PHP.

Symfony can be used to develop all kind of websites,
from your personal blog to high traffic ones like Dailymotion or Yahoo! Answers.

%prep
%setup -q -n %{php_name}-%{version}

%build
true

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/php/Symfony
%{__cp} -R src/Symfony/* %{buildroot}%{_datadir}/php/Symfony

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%doc CONTRIBUTORS.md
%doc CHANGELOG-2.0.md
%doc LICENSE
%doc README.md
%doc UPDATE.ja.md
%doc UPDATE.md
%{_datadir}/php/Symfony

%changelog
*  Wed Oct 26 2011 Tavis Aitken <tavisto@tavisto.net> - 2.0.4-1
- Initial build