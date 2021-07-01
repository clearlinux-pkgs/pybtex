#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybtex
Version  : 0.22.2
Release  : 27
URL      : https://files.pythonhosted.org/packages/74/73/cbb788404c1b90e7b15f411e60eadeb67965d36a0738775ca031931fedd1/pybtex-0.22.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/73/cbb788404c1b90e7b15f411e60eadeb67965d36a0738775ca031931fedd1/pybtex-0.22.2.tar.gz
Summary  : A BibTeX-compatible bibliography processor in Python
Group    : Development/Tools
License  : MIT
Requires: pybtex-bin = %{version}-%{release}
Requires: pybtex-license = %{version}-%{release}
Requires: pybtex-python = %{version}-%{release}
Requires: pybtex-python3 = %{version}-%{release}
Requires: PyYAML
Requires: latexcodec
Requires: six
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : latexcodec
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
==================================================
        
        Synopsis
        --------

%package bin
Summary: bin components for the pybtex package.
Group: Binaries
Requires: pybtex-license = %{version}-%{release}

%description bin
bin components for the pybtex package.


%package license
Summary: license components for the pybtex package.
Group: Default

%description license
license components for the pybtex package.


%package python
Summary: python components for the pybtex package.
Group: Default
Requires: pybtex-python3 = %{version}-%{release}

%description python
python components for the pybtex package.


%package python3
Summary: python3 components for the pybtex package.
Group: Default
Requires: python3-core
Provides: pypi(pybtex)
Requires: pypi(latexcodec)
Requires: pypi(pyyaml)
Requires: pypi(six)

%description python3
python3 components for the pybtex package.


%prep
%setup -q -n pybtex-0.22.2
cd %{_builddir}/pybtex-0.22.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594835705
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybtex
cp %{_builddir}/pybtex-0.22.2/COPYING %{buildroot}/usr/share/package-licenses/pybtex/144ddab7f73855648bab2887dd14e753fe1407a5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybtex
/usr/bin/pybtex-convert
/usr/bin/pybtex-format

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybtex/144ddab7f73855648bab2887dd14e753fe1407a5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
