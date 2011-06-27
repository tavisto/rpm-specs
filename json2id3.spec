Name:           json2id3
Version:        0.1.0
Release:        1%{?dist}
Summary:        Id3 tag utility using a json file as the source for tags

Group:          Applications/Multimedia 
License:        MIT 
URL:            https://github.com/tavisto/json2id3 
Source0:        https://github.com/downloads/tavisto/json2id3/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: taglib-devel
BuildRequires: libjson-devel 
BuildRequires: cmake 
Requires:      taglib 
Requires:      libjson 

%description
Id3 tag utility using a json file as the source for tags
Currently only supports aif files


%prep
%setup -q


%build
mkdir %{_target_platform} 
pushd %{_target_platform} 
%cmake ..
popd
make %{?_smp_mflags} -C %{_target_platform} 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/json2id3


%changelog
* Sun Jun 26 2011 Tavis Aitken <tavisto@tavisto.net> - 0.1.0-1
- Initial package
