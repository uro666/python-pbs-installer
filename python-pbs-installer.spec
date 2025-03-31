%define module pbs-installer
%define uname pbs_installer

Name:		python-pbs-installer
Version:	2025.3.17
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pbs-installer/%{uname}-%{version}.tar.gz
Summary:	Installer for Python Build Standalone
URL:		https://pypi.org/project/pbs-installer/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)

%description
Installer for Python Build Standalone

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py_install


%files
%{_bindir}/pbs-install
%{py_sitedir}/%{uname}
%{py_sitedir}/%{uname}-*.*-info
