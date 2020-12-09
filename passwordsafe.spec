%global		pwsafe_release	1.12.0
%global		debug_package	%{nil}


Name:		passwordsafe
Version:	1.12.0
Release:	1%{?dist}
Summary:	Password Safe is a password database utility
Group:		Applications/Utils

License:	Artistic 2.0
URL:		http://pwsafe.org/
Vendor:		Rony Shapiro

Source0:	https://github.com/pwsafe/pwsafe/archive/%{pwsafe_release}.tar.gz#/pwsafe-%{pwsafe_release}.tar.gz

Conflicts:	pwsafe
%{?el7:BuildRequires: epel-release}
BuildRequires:	make, cmake, gcc-c++, zip, gettext, desktop-file-utils, perl
BuildRequires:	qrencode-devel, openssl-devel, libcurl-devel, file-devel, libuuid-devel
#BuildRequires:	libXt-devel, libXtst-devel, wxGTK3-devel
#BuildRequires:	libyubikey-devel, ykpers-devel, xerces-c-devel
%{?el7:#Requires: epel-release, wxBase3, wxGTK3, xerces-c, ykpers}

# Errors:

# ELN:
# No matching package to install: 'libyubikey-devel'
# No matching package to install: 'ykpers-devel'

# Stream8 and CentOS 7
# No matching package to install: 'libyubikey-devel'
# No matching package to install: 'wxGTK3-devel'
# No matching package to install: 'xerces-c-devel'
# No matching package to install: 'ykpers-devel'

# Mageia:
# No matching package to install: 'libXt-devel'
# No matching package to install: 'libXtst-devel'
# No matching package to install: 'libyubikey-devel'
# No matching package to install: 'wxGTK3-devel'

# OpenSuse:
# No matching package to install: 'xerces-c-devel'
# No matching package to install: 'ykpers-devel'

%description
Password Safe is a password database utility. Like many other such products,
commercial and otherwise, it stores your passwords in an encrypted file,
allowing you to remember only one password (the "safe combination"), instead of
all the user name / password combinations that you use.

%prep

%setup -q -n pwsafe-%{pwsafe_release}
mv install/desktop/fedora-pwsafe.desktop install/desktop/passwordsafe.desktop

ls -l /etc/yum.repos.d/
grep '' /etc/yum.repos.d/*
# Jonny Was here

%build

# EL7:
%{?el7:%global cmake_opt -D wxWidgets_CONFIG_EXECUTABLE=/usr/libexec/wxGTK3/wx-config}

mkdir -p build
cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DNO_GTEST:BOOL=ON %{cmake_opt} ..
if [[ -d %{_host_alias} ]] ; then
  cd %{_host_alias}
fi
make %{?_smp_mflags}
cd %{_builddir}/%{buildsubdir}

%install

rm -rf %{buildroot}

mkdir -p build
cd build
if [[ -d %{_host_alias} ]] ; then
  cd %{_host_alias}
fi
make install DESTDIR=%{buildroot}
cd %{_builddir}/%{buildsubdir}

# Manually install the icon
install -p -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 install/graphics/pwsafe.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

# Remove the superfluous .desktop file
rm %{buildroot}%{_datadir}/applications/pwsafe.desktop
# Install the real desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications install/desktop/passwordsafe.desktop

%find_lang pwsafe

%clean
rm -rf %{buildroot}

%post
%postun
%docdir /usr/share/doc/passwordsafe
%ghost docs/*

%files -f pwsafe.lang

%license LICENSE
%doc install/copyright
%doc docs/ReleaseNotes.md

%{_datadir}/man/man1/pwsafe.1.gz
%{_datadir}/icons/hicolor/48x48/apps/pwsafe.png
%{_datadir}/applications/passwordsafe.desktop
%{_bindir}/pwsafe
%{_bindir}/pwsafe-cli

%dir %{_datadir}/passwordsafe
%dir %{_datadir}/passwordsafe/xml
%{_datadir}/passwordsafe/xml/KPX0_to_PWS.xslt
%{_datadir}/passwordsafe/xml/KPV1_to_PWS.xslt
%{_datadir}/passwordsafe/xml/KPV2_to_PWS.xslt
%{_datadir}/passwordsafe/xml/pwsafe.xsl
%{_datadir}/passwordsafe/xml/pwsafe.xsd
%{_datadir}/passwordsafe/xml/pwsafe_filter.xsd
%dir %{_datadir}/passwordsafe/help
%{_datadir}/passwordsafe/help/helpPL.zip
%{_datadir}/passwordsafe/help/helpZH.zip
%{_datadir}/passwordsafe/help/helpES.zip
%{_datadir}/passwordsafe/help/helpEN.zip
%{_datadir}/passwordsafe/help/helpDE.zip
%{_datadir}/passwordsafe/help/helpFR.zip
%{_datadir}/passwordsafe/help/helpRU.zip


%changelog
* Sat Dec 05 2020 João Carlos Mendes Luís - 1.12.0
- Copied from release 2019-11-04, Simon Gerhards - 1.08.3-0.git05fef0b4c
- New upstream release, 1.12.0

# vim:nosmarttab:noexpandtab
