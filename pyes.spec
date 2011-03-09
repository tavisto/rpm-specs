%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           pyes
Version:        0.14.1
Release:        1%{?dist}
Summary:        A connector to use elasticsearch from python 

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/pyes 
Source0:        http://pypi.python.org/packages/source/p/pyes/pyes-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch 
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:        python

%description
pyes is a connector to use elasticsearch from python

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc README
%doc README.rst
%doc LICENSE
%doc THANKS
%doc Changelog
%doc TODO
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}*

%changelog
* Mon Mar  7 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.1-1
- Iniitial package 
