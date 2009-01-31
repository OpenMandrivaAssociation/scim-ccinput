%define version   0.3.1
%define release   %mkrel 5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:      scim-ccinput
Summary:   SCIM IMEngine module for CCInput
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://www.scim-im.org
Source0:   %{name}-%{version}.tar.bz2
Patch0:	scim-ccinput-0.3.1-gcc43.patch
Patch1: scim-ccinput-0.3.1-linkage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:   scim-devel >= 1.4.7-3mdk
BuildRequires:   automake, libltdl-devel
Obsoletes: %{libname}
Requires: scim-client = %scim_api

%description
Scim-ccinput is an SCIM IMEngine module for CCInput.
CCInput is another Pinyin input method for Chinese.

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .link

%build
%configure2_5x --disable-skim-support
%make

%install
rm -rf $RPM_BUILD_ROOT
# fix rpmlint warnings:
chmod -x AUTHORS ChangeLog COPYING README
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}%{scim_plugins_dir}/*/*.{a,la}

%find_lang ccinput

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -f ccinput.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/ccinput/*
%{_datadir}/scim/icons/*.png
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
