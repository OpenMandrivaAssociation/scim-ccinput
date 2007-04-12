%define version   0.3.1
%define release   %mkrel 1

%define scim_version   1.4.0

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        %{libname} = %{version}-%{release}
Requires:        scim >= %{scim_version}
BuildRequires:   scim-devel >= %{scim_version}
BuildRequires:   automake1.8, libltdl-devel

%description
Scim-ccinput is an SCIM IMEngine module for CCInput.
CCInput is another Pinyin input method for Chinese.


%package -n %{libname}
Summary:    Scim-ccinput library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
scim-ccinput library.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x --disable-skim-support
%make

%install
rm -rf $RPM_BUILD_ROOT
# fix rpmlint warnings:
chmod -x AUTHORS ChangeLog COPYING README
%makeinstall_std mkinstalldirs='mkdir -p'

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/scim-1.0/*/*.{a,la}

%find_lang ccinput

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f ccinput.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/ccinput/*
%{_datadir}/scim/icons/*.png

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/IMEngine/*.so
%{_libdir}/scim-1.0/SetupUI/*.so


