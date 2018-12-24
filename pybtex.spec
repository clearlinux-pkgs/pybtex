#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybtex
Version  : 0.22.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/e4/65/e4a9a368783e61e29645c7faff066e451dcdf5dbb8e80f258d6a9c474e24/pybtex-0.22.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/65/e4a9a368783e61e29645c7faff066e451dcdf5dbb8e80f258d6a9c474e24/pybtex-0.22.0.tar.gz
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

%description python3
python3 components for the pybtex package.


%prep
%setup -q -n pybtex-0.22.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545682255
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybtex
cp COPYING %{buildroot}/usr/share/package-licenses/pybtex/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybtex
/usr/bin/pybtex-convert
/usr/bin/pybtex-format

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybtex/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
