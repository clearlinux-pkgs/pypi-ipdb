#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipdb
Version  : 0.13.9
Release  : 44
URL      : https://files.pythonhosted.org/packages/fc/56/9f67dcd4a4b9960373173a31be1b8c47fe351a1c9385677a7bdd82810e57/ipdb-0.13.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/56/9f67dcd4a4b9960373173a31be1b8c47fe351a1c9385677a7bdd82810e57/ipdb-0.13.9.tar.gz
Summary  : IPython-enabled pdb
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ipdb-bin = %{version}-%{release}
Requires: pypi-ipdb-license = %{version}-%{release}
Requires: pypi-ipdb-python = %{version}-%{release}
Requires: pypi-ipdb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(decorator)
BuildRequires : pypi(ipython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(toml)

%description
=============

%package bin
Summary: bin components for the pypi-ipdb package.
Group: Binaries
Requires: pypi-ipdb-license = %{version}-%{release}

%description bin
bin components for the pypi-ipdb package.


%package license
Summary: license components for the pypi-ipdb package.
Group: Default

%description license
license components for the pypi-ipdb package.


%package python
Summary: python components for the pypi-ipdb package.
Group: Default
Requires: pypi-ipdb-python3 = %{version}-%{release}

%description python
python components for the pypi-ipdb package.


%package python3
Summary: python3 components for the pypi-ipdb package.
Group: Default
Requires: python3-core
Provides: pypi(ipdb)
Requires: pypi(decorator)
Requires: pypi(ipython)
Requires: pypi(setuptools)
Requires: pypi(toml)

%description python3
python3 components for the pypi-ipdb package.


%prep
%setup -q -n ipdb-0.13.9
cd %{_builddir}/ipdb-0.13.9
pushd ..
cp -a ipdb-0.13.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399471
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipdb
cp %{_builddir}/ipdb-0.13.9/COPYING.txt %{buildroot}/usr/share/package-licenses/pypi-ipdb/eac15b69f9f0a12e02459ba5c6be4fa52c10f364
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipdb3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipdb/eac15b69f9f0a12e02459ba5c6be4fa52c10f364

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
