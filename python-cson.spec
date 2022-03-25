#
# Conditional build:
%bcond_with	tests	# unit tests (test data not included in release tarballs)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Parser for Coffeescript Object Notation (CSON)
Summary(pl.UTF-8):	Parser formatu CSON (Coffeescript Object Notation)
Name:		python-cson
Version:	0.8
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cson/
Source0:	https://files.pythonhosted.org/packages/source/c/cson/cson-%{version}.tar.gz
# Source0-md5:	02f738b7f765e88b4222fe2126a685db
URL:		https://pypi.org/project/cson/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-speg
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-speg
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python parser for the Coffeescript Object Notation (CSON).

%description -l pl.UTF-8
Pythonowy parser formatu CSON (Coffeescript Object Notation - notacji
obiektów z języka Coffeescript).

%package -n python3-cson
Summary:	Parser for Coffeescript Object Notation (CSON)
Summary(pl.UTF-8):	Parser formatu CSON (Coffeescript Object Notation)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-cson
A Python parser for the Coffeescript Object Notation (CSON).

%description -n python3-cson -l pl.UTF-8
Pythonowy parser formatu CSON (Coffeescript Object Notation - notacji
obiektów z języka Coffeescript).

%prep
%setup -q -n cson-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/cson
%{py_sitescriptdir}/cson-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cson
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/cson
%{py3_sitescriptdir}/cson-%{version}-py*.egg-info
%endif
