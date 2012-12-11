%define	pkgname image
%define name	octave-%{pkgname}
%define version 1.0.14

Summary:	Image processing toolkit for Octave
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/image/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
BuildRequires:  octave-devel >= 3.2.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:	jpeg-devel

%description
This package provides Octave functions for feature extraction, image
statistics, spatial and geometric transformations, morphological
operations, linear filtering, and much more.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}



%changelog
* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 1.0.14-1mdv2011.0
+ Revision: 687978
- import octave-image


