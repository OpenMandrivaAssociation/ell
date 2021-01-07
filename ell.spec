%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		ell
Version:	0.36
Release:	1
Summary:	Embedded Linux library
License:	LGPLv2+
Group:		System/Libraries
URL:		https://01.org/ell
Source0:	https://www.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz

# https://lore.kernel.org/lkml/20180924094723.487697-1-lkundrak@v3.sk/T/#u
Source1:	https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/keyctl.h?h=v4.6#/keyctl.h

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
[ ! -d linux ] && mkdir linux
cp -p -f %{SOURCE1} linux/keyctl.h

%build
%configure
%make_build LDFLAGS="%{ldflags} -ldl"

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
