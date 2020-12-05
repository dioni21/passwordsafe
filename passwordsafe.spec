%global commit_short 05fef0b4c

Name:           passwordsafe
Version:        1.08.3
Release:        0.git%{commit_short}%{?dist}
Summary:        Password Safe is a password database utility

License:        Artistic 2.0
URL:            http://pwsafe.org/

#from a git snapshot:
#export commit=$(git rev-parse --short HEAD)
#git archive --format=tar --prefix=passwordsafe-git$commit/ $commit | xz > passwordsafe-git$commit.tar.xz
Source0:        passwordsafe-git%{commit_short}.tar.xz

Conflicts:      pwsafe
BuildRequires:  cmake, gcc-c++, libXt-devel, libXtst-devel, libuuid-devel, libyubikey-devel, xerces-c-devel, wxGTK3-devel, ykpers-devel, zip, gettext, desktop-file-utils, qrencode-devel, perl, openssl-devel, libcurl-devel, file-devel


%description
Password Safe is a password database utility. Like many other such products,
commercial and otherwise, it stores your passwords in an encrypted file,
allowing you to remember only one password (the "safe combination"), instead of
all the user name / password combinations that you use.


%prep
%setup -q -n passwordsafe-git%{commit_short}

%build
mkdir build
pushd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DNO_GTEST:BOOL=ON ..
make %{?_smp_mflags}
mv %{_builddir}/%{buildsubdir}/install/desktop/fedora-pwsafe.desktop %{_builddir}/%{buildsubdir}/install/desktop/passwordsafe.desktop


%install
rm -rf %{buildroot}

pushd build
make install DESTDIR=%{buildroot}
popd # build

# Manually install the icon
rm %{buildroot}/%{_datadir}/pixmaps/pwsafe.png
install -p -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{_builddir}/%{buildsubdir}/install/graphics/pwsafe.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

# Manually install the help files
install -p -d -m 755 %{buildroot}%{_datadir}/doc/passwordsafe/help
install -p -m 644 %{_builddir}/%{buildsubdir}/build/help/help*.zip %{buildroot}%{_datadir}/doc/passwordsafe/help

# Remove the superfluous .desktop file
rm %{buildroot}/%{_datadir}/applications/pwsafe.desktop
# Install the real desktop file
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications  %{_builddir}/%{buildsubdir}/install/desktop/passwordsafe.desktop

%find_lang pwsafe


%files -f pwsafe.lang
%license LICENSE

%{_datadir}/passwordsafe
%{_datadir}/doc/passwordsafe
%{_datadir}/man/man1/pwsafe.1.gz
%{_datadir}/icons/hicolor/48x48/apps/pwsafe.png
%{_datadir}/applications/passwordsafe.desktop
%{_bindir}/pwsafe
%{_bindir}/pwsafe-cli


%changelog
* Mon Nov 04 2019 Simon Gerhards - 1.08.3-0.git05fef0b4c
- New upstream snapsot

* Thu Jul 18 2019 Simon Gerhards - 1.08.2-1.git00272cc29
- Upstream version 1.08.2

* Fri May 03 2019 Simon Gerhards - 1.08-1.gitd2665f8db
- Rebuilt from release tag

* Tue Apr 30 2019 Simon Gerhards - 1.08-0.1.pre.gitf90d81a38
- New upstream snapshot
- Add passwordsafe-cli binary

* Sun Dec 30 2018 Simon Gerhards - 1.07-1.git632eec95a
- Upstream version 1.07

* Sun Aug 26 2018 Simon Gerhards - 1.06-1.gita4e0e83c2
- Upstream version 1.06

* Tue Apr 17 2018 Simon Gerhards - 1.05-1.git7bf1203f8
- Upstream version 1.05

* Sun Jan 21 2018 Simon Gerhards - 1.04-1.git24581db35
- Upstream version 1.04

* Sun Dec 24 2017 Simon Gerhards - 1.03-2.git99b679685
- Newer upstream snapshot

* Sat Oct 14 2017 Simon Gerhards - 1.03-1.git521e05324
- Upstream version 1.03

* Tue Oct 03 2017 Simon Gerhards - 1.02.1-2.gitda3d5e5f9
- Use cmake build macro
- Newer upstream snapshot

* Mon May 01 2017 Simon Gerhards - 1.02.1-1.git308bf30e7
- Upstream versrion 1.02.1
- Drop Wayland workaround

* Mon Apr 10 2017 Simon Gerhards - 1.02-1.git169a6dc2f
- Upstream versrion 1.02

* Sat Jan 21 2017 Simon Gerhards - 1.01-2.git913d7ac
- Work around crash under Wayland

* Wed Dec 28 2016 Simon Gerhards - 1.01-1.git913d7ac
- Upstream version 1.01

* Thu Oct 06 2016 Simon Gerhards - 1.0-1.git148aa00
- Upstream version 1.00

* Fri Jul 08 2016 Simon Gerhards - 0.99-1.git3153677
- Upstream version 0.99

* Sun Jul 03 2016 Simon Gerhards - 0.98.1-2.git7787e78
- New git snapshot
- Use cmake build and install system

* Fri Mar 18 2016 Simon Gerhards - 0.98.1-1.giteea4ef6
- New upstream version 0.98.1 + some commits

* Sun Jan 24 2016 Simon Gerhards - 0.98-1.git3643054
- Upstream version 0.98

* Thu Nov 12 2015 Simon Gerhards - 0.97-2.git2b4d25c
- New git snapshot

* Fri Oct 09 2015 Simon Gerhards - 0.97-1.git6e591b9
- New git snapshot

* Mon Aug 10 2015 Simon Gerhards - 0.96-1.git2abf291
- New git snapshot

* Wed Apr 22 2015 Simon Gerhards - 0.95.1-2.git38456e0
- New git snapshot

* Wed Feb 11 2015 Simon Gerhards - 0.95.1-1.gitef36d39
- Upstream version 0.95.1

* Sat Dec 20 2014 Simon Gerhards - 094.1-1.gitfea11aa
- Upstream version 0.94.1 from branch 'BR1220'

* Sat Jul 26 2014 Simon Gerhards - 0.94-1.gitabef793
- Upstream version 0.94

* Mon Apr 21 2014 Simon Gerhards - 0.93.1-1.gitf8710e3
- new git snapshot

* Mon Mar 17 2014 Simon Gerhards - 0.93-3.git36e01ec
- new git snapshot

* Tue Feb 18 2014 Simon Gerhards - 0.93-2.gite4a571
- new git snapshot

* Fri Feb 14 2014 Simon Gerhards - 0.93-1.gita0ca83
- upstream version 0.93BETA + a few commits
- use standard build options
- drop date -- use abbreviated commit hash instead and append it to Release
  instead of Version

* Fri Jan 31 2014 Simon Gerhards - 0.92.git20140131-1
- newer git snapshot
- replaced the git snapsot date seperator: '+' -> '.'
- switched to a xz compressed source tarball

* Mon Jan 20 2014 Simon Gerhards - 0.92+git20140117-3
- renamed .desktop file to passwordsafe.desktop
- further spec file tweaks

* Sun Jan 19 2014 Simon Gerhards - 0.92+git20140117-2
- spec file tweaks

* Fri Jan 17 2014 Simon Gerhards - 0.92+git20140117-1
- Initial version
