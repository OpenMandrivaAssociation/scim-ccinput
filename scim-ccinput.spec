%define version   0.3.1
%define release   %mkrel 2

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
BuildRequires:   scim-devel >= 1.4.7-3mdk
BuildRequires:   automake, libltdl-devel

%description
Scim-ccinput is an SCIM IMEngine module for CCInput.
CCInput is another Pinyin input method for Chinese.


%package -n %{libname}
Summary:    Scim-ccinput library
Group:      System/Internationalization

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
rm -f %{buildroot}%{scim_plugins_dir}/*/*.{a,la}

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
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
