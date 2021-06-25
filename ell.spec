%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Embedded Linux library
Name:		ell
Version:	0.41
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		https://01.org/ell
Source0:	https://www.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz
Patch0:		ell-0.39-fix-build-with-clang.patch

%description
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
%{description}

%package -n %{develname}
Summary:	Embedded Linux library development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Headers for developing against libell.

%prep
%autosetup -p1

%build
%configure
%make_build LDFLAGS="%{build_ldflags} -ldl"

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%files -n %{libname}
%{_libdir}/libell.so.%{major}*

%files -n %{develname}
%license COPYING
%doc AUTHORS README TODO ChangeLog
%{_includedir}/ell
%{_libdir}/libell.so
%{_libdir}/pkgconfig/ell.pc
