%define name picard
%define version 0.7.2
%define release %mkrel 3

Summary: Musicbrainz Tagger
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://helixcommunity.org/frs/download.php/2252/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://musicbrainz.org/doc/PicardTagger
BuildRequires: python-devel
BuildRequires: desktop-file-utils
Requires: python-tunepimp
Requires: python-musicbrainz2
Requires: wxpython2.6
Requires: tunepimp-plugins
BuildArch: noarch



%description
This is an audio file tagger based on musicbrainz.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT
%find_lang %name
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog TODO
%_bindir/%name
%py_puresitedir/picard*
%_datadir/applications/%name.desktop
%_datadir/icons/*


