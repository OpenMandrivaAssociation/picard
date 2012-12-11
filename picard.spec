Summary:	MusicBrainz-based audio tagger
Name:		picard
Version:	1.1
Release:	%mkrel 1
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Url:		http://musicbrainz.org/doc/PicardTagger
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz

Source1:	http://users.musicbrainz.org/~luks/picard-plugins/discnumber.py
Source2:	http://users.musicbrainz.org/~luks/picard-plugins/featartist.py
Source3:	http://users.musicbrainz.org/~luks/picard-plugins/coverart.py
#gw old API:
#Source4:	http://dispuut-ivv.nl/~jan/bonusdisc.py
#http://users.musicbrainz.org/~luks/picard-plugins/lastfm/
Source5:	lastfm.tar.bz2
Source6:	http://gitorious.org/musicbrainz/addrelease/blobs/raw/master/addrelease.py
Source7:	http://users.musicbrainz.org/~luks/picard-plugins/cuesheet.py
#gw old API:
#Source8:	http://foolip.org/mb/encoding.py
# search plugins https://github.com/brianfreud/Picard-plugins
Source9:	SearchAMG.py
Source10:	SearchDiscogs3.py
Source11:	SearchAmazon3.py
Source12:	SearchCastAlbums3.py
Source13:	SearchFilmMusziek3.py
Source14:	SearchGMR.py
Source15:	SearchGoogle3.py
Source16:	SearchLortelArchives3.py
Source17:	SearchSoundtrackCollector3.py
Source18:	SearchSoundtrackINFO3.py
Source100:	SearchEbay.py
#
Source19: http://users.musicbrainz.org/~luks/picard-plugins/open_in_gui.py
Source20: http://users.musicbrainz.org/~luks/picard-plugins/titlecase.py
Source21: http://users.musicbrainz.org/~luks/picard-plugins/release_type.py
Source22: http://users.musicbrainz.org/~luks/picard-plugins/featartistsintitles.py
# http://forums.musicbrainz.org/viewtopic.php?id=2949
Source23: lastfmplus-0.13.zip
Source24: http://users.musicbrainz.org/~luks/picard-plugins/classicdiscnumber.py
Source25: http://users.musicbrainz.org/~luks/picard-plugins/swapprefix.py
Source26: http://kalou.net/unix/picard/metaflac_rgscan.py
Source27: http://users.musicbrainz.org/~luks/picard-plugins/no_release.py
Source28: http://github.com/voiceinsideyou/creaps-picard-plugins/raw/master/titleversion.py
Source29: http://github.com/voiceinsideyou/creaps-picard-plugins/raw/master/titlesort.py
Source30: https://github.com/voiceinsideyou/picard/raw/plugins/contrib/plugins/removeperfectalbums.py
Source31: https://raw.github.com/encukou/picard-plugins/master/autosave.py
Patch0:		picard-1.0-avutil-linking.patch
%py_requires -d
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	python-qt4-core >= 4.3
BuildRequires:	mutagen > 1.11
BuildRequires:	libofa-devel
BuildRequires:	libexpat-devel
BuildRequires:	ffmpeg-devel
Requires:	python-qt4-core >= 4.3
Requires:	python-qt4-gui >= 4.3
Requires:	python-qt4-network >= 4.3
Requires:	python-qt4-xml >= 4.3
Requires:	python-sip
Requires:	mutagen > 1.9
Requires:	libdiscid
#gw for metaflac:
Suggests:	flac
#gw for fpcalc (AcoustID calculation)
Suggests:	chromaprint


%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%setup -q -n %name-%version
%apply_patches

%build
env %{__python} setup.py config
env CFLAGS="%{optflags} -I%_includedir/libavcodec -I%_includedir/libavformat" %{__python} setup.py build

# (tpg) it fails for now
#%check
#%{__python} setup.py test

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
install -D picard.desktop %buildroot%_datadir/applications/picard.desktop 
sed -i -e 's/^Icon=%{name}-32.png$/Icon=%{name}-32/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--remove-category="Application" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*
	

%define PLUGINDIR %{buildroot}%{python_sitearch}/picard/plugins/

install -pm 0644 %{SOURCE1} %{PLUGINDIR}
install -pm 0644 %{SOURCE2} %{PLUGINDIR}
install -pm 0644 %{SOURCE3} %{PLUGINDIR}
#install -pm 0644 %{SOURCE4} %{PLUGINDIR}
tar -xjf %{SOURCE5} -C %{PLUGINDIR}
install -pm 0644 %{SOURCE6} %{PLUGINDIR}
install -pm 0644 %{SOURCE7} %{PLUGINDIR}
#install -pm 0644 %{SOURCE8} %{PLUGINDIR}

install -pm 0644 %{SOURCE9} %{PLUGINDIR}
install -pm 0644 %{SOURCE10} %{PLUGINDIR}
install -pm 0644 %{SOURCE11} %{PLUGINDIR}
install -pm 0644 %{SOURCE12} %{PLUGINDIR}
install -pm 0644 %{SOURCE13} %{PLUGINDIR}
install -pm 0644 %{SOURCE14} %{PLUGINDIR}
install -pm 0644 %{SOURCE15} %{PLUGINDIR}
install -pm 0644 %{SOURCE16} %{PLUGINDIR}
install -pm 0644 %{SOURCE17} %{PLUGINDIR}
install -pm 0644 %{SOURCE18} %{PLUGINDIR}
install -pm 0644 %{SOURCE100} %{PLUGINDIR}
#gw fix API versions:
#sed -i "s^\"0.10\"^\"%version\"^" %{PLUGINDIR}/Search*


install -pm 0644 %{SOURCE19} %{PLUGINDIR}
install -pm 0644 %{SOURCE20} %{PLUGINDIR}
install -pm 0644 %{SOURCE21} %{PLUGINDIR}
install -pm 0644 %{SOURCE22} %{PLUGINDIR}

unzip %{SOURCE23} -d %{PLUGINDIR}
install -pm 0644 %{SOURCE24} %{PLUGINDIR}
install -pm 0644 %{SOURCE25} %{PLUGINDIR}
install -pm 0644 %{SOURCE26} %{PLUGINDIR}
#gw fix metaflac path
sed -i "s^/sw/bin/metaflac^/usr/bin/metaflac^" %{PLUGINDIR}/metaflac_rgscan.py
install -pm 0644 %{SOURCE27} %{PLUGINDIR}
install -pm 0644 %{SOURCE28} %{PLUGINDIR}
install -pm 0644 %{SOURCE29} %{PLUGINDIR}
install -pm 0644 %{SOURCE30} %{PLUGINDIR}
install -pm 0644 %{SOURCE31} %{PLUGINDIR}


%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS.txt NEWS.txt INSTALL.txt
%{_bindir}/picard
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/picard.png
%{python_sitearch}/*egg-info
%dir %{python_sitearch}/picard
%{python_sitearch}/picard/*


%changelog
* Tue Sep 04 2012 Götz Waschk <waschk@mandriva.org> 1.1-1mdv2012.0
+ Revision: 816304
- new version
- drop patch 1
- remove updated German translation
- update Search plugins

* Mon Jun 11 2012 Götz Waschk <waschk@mandriva.org> 1.0-4
+ Revision: 804397
- add patch for ffmpeg 0.11
- suggest chromaprint for audio fingerprinting

* Mon Jun 04 2012 Götz Waschk <waschk@mandriva.org> 1.0-3
+ Revision: 802439
- fix broken German translation

* Sun Jun 03 2012 Götz Waschk <waschk@mandriva.org> 1.0-2
+ Revision: 802174
- rebuild
- fix build deps
- new version
- update the patch
- update featartist, metaflac, coverart, featartistintitles plugins
- add removeperfectalbums and autosave plugins

* Sun Jan 01 2012 Götz Waschk <waschk@mandriva.org> 0.16-2
+ Revision: 748606
- add more plugins

* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 0.16-1
+ Revision: 707227
- new version
- add new plugins:
  * Last.fm.Plus
  * Classic Disc Numbers
  * MetaFlac ReplayGain
  * No release
  * swapprefix function
- suggest flac for metaflac plugin
- new version

* Fri Jul 22 2011 Götz Waschk <waschk@mandriva.org> 0.15-2
+ Revision: 690917
- add new version of addrelease plugin
- add new plugins: Open in GUI, Title Case, Release Type, feat. in title

* Thu Jul 21 2011 Götz Waschk <waschk@mandriva.org> 0.15-1
+ Revision: 690846
- new version
- update plugins
- disable outdated plugins (encoding, bonus disk)

* Tue May 24 2011 Götz Waschk <waschk@mandriva.org> 0.14-1
+ Revision: 678125
- new version
- patch to fix linking

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 0.12.1-2mdv2011.0
+ Revision: 591470
- rebuild for new python 2.7

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2011.0
+ Revision: 460729
- new version
- update file list

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2010.0
+ Revision: 441782
- rebuild

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.11-2mdv2009.1
+ Revision: 320490
- rebuild for new python

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 0.11-1mdv2009.1
+ Revision: 309982
- new version
- add some new plugins

* Thu Oct 16 2008 Götz Waschk <waschk@mandriva.org> 0.10-3mdv2009.1
+ Revision: 294374
- rebuild for new libdiscid

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2009.0
+ Revision: 268965
- rebuild early 2009.0 package (before pixel changes)

* Fri Aug 08 2008 Götz Waschk <waschk@mandriva.org> 0.10-1mdv2009.0
+ Revision: 268040
- new version
- update plugins (sources 1-5)
- drop plugins (sources 6-18)
- update deps

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 0.9.0-6mdv2009.0
+ Revision: 199392
- fix build with new ffmpeg

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Wed Jan 02 2008 Götz Waschk <waschk@mandriva.org> 0.9.0-5mdv2008.1
+ Revision: 140410
- rebuild for new ffmpeg

* Fri Dec 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-4mdv2008.1
+ Revision: 138712
- add missing python-qt4-* requires
- add libffmpeg as a buildrequire - this should allow to calculate audio files fingerprints

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-3mdv2008.1
+ Revision: 138631
- fix instalation of additional plugins

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-2mdv2008.1
+ Revision: 138575
- do not require whole python-qt4 packages, only core one is needed

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 138236
- rewrite whole spec file
- add missing buildrequires, remove not needed ones
- compile with optflags
- new license policy
- add some plugins
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 11 2007 Götz Waschk <waschk@mandriva.org> 0.7.2-3mdv2008.0
+ Revision: 26222
- use wxpython2.6


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-2mdv2007.0
+ Revision: 88386
- update file list

* Sat Nov 25 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.1
+ Revision: 87254
- Import picard

* Sat Nov 25 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.1
- initial package

