%global pypi_name fasteners

Name:           python-%{pypi_name}
Version:        0.20
Release:        2
Group:          Development/Python
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(six)
BuildRequires:  python%{pyver}dist(monotonic)
BuildRequires:  python%{pyver}dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
A python package that provides useful locks.

%files
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
