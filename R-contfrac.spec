#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-contfrac
Version  : 1.1.12
Release  : 37
URL      : https://cran.r-project.org/src/contrib/contfrac_1.1-12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/contfrac_1.1-12.tar.gz
Summary  : Continued Fractions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-contfrac-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-contfrac package.
Group: Libraries

%description lib
lib components for the R-contfrac package.


%prep
%setup -q -c -n contfrac
cd %{_builddir}/contfrac

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640992838

%install
export SOURCE_DATE_EPOCH=1640992838
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library contfrac
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library contfrac
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library contfrac
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc contfrac || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/contfrac/DESCRIPTION
/usr/lib64/R/library/contfrac/INDEX
/usr/lib64/R/library/contfrac/Meta/Rd.rds
/usr/lib64/R/library/contfrac/Meta/features.rds
/usr/lib64/R/library/contfrac/Meta/hsearch.rds
/usr/lib64/R/library/contfrac/Meta/links.rds
/usr/lib64/R/library/contfrac/Meta/nsInfo.rds
/usr/lib64/R/library/contfrac/Meta/package.rds
/usr/lib64/R/library/contfrac/NAMESPACE
/usr/lib64/R/library/contfrac/R/contfrac
/usr/lib64/R/library/contfrac/R/contfrac.rdb
/usr/lib64/R/library/contfrac/R/contfrac.rdx
/usr/lib64/R/library/contfrac/help/AnIndex
/usr/lib64/R/library/contfrac/help/aliases.rds
/usr/lib64/R/library/contfrac/help/contfrac.rdb
/usr/lib64/R/library/contfrac/help/contfrac.rdx
/usr/lib64/R/library/contfrac/help/paths.rds
/usr/lib64/R/library/contfrac/html/00Index.html
/usr/lib64/R/library/contfrac/html/R.css
/usr/lib64/R/library/contfrac/tests/aaa.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/contfrac/libs/contfrac.so
/usr/lib64/R/library/contfrac/libs/contfrac.so.avx2
/usr/lib64/R/library/contfrac/libs/contfrac.so.avx512
