%define octpkg image

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Image processing toolkit for Octave
Name:		octave-%{octpkg}
Version:	2.6.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image package provides functions for processing images.
The package also provides functions for feature extraction, image
statistics, spatial and geometric transformations, morphological operations,
linear filtering, and much more.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

