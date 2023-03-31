%global pypi_name fasteners

Name:           python-%{pypi_name}
Version:        0.15
Release:        3
Group:          Development/Python
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(monotonic)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
A python package that provides useful locks.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.rst
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info/
