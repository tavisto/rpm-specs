%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           hgkerberos
Version:        0.0.1
Release:        2%{?dist}
Summary:        Provides support for kerberos authentication over HTTP

License:        ASL 2.0 
URL:            https://bitbucket.org/tolsen/hgkerberos
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64 
BuildRequires:  python-devel

Requires:       python-kerberos
Requires:       python-urllib2_kerberos
Requires:       mercurial

%description
hgkerberos provides support for kerberos authentication
(Negotiate/SPNEGO) over HTTP

%prep
%setup -q -n %{name}-%{version}


%build
true


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{python_sitearch}/hgext
%{__cp} kerberos.py %{buildroot}%{python_sitearch}/hgext/


%files
%doc README
%doc COPYING
%{python_sitearch}/hgext/kerberos.*



%changelog
* Fri Jul 20 2012 Tavis Aitken <tavisto@tavisto.net> - 0.0.1-1
- Initial build

* Fri Jul 20 2012 Tavis Aitken <tavisto@tavisto.net> - 0.0.1-2
- Fixed the package to be arch specific just like the mercurial package
