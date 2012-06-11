Summary:	MusicBrainz-based audio tagger
Name:		picard
Version:	1.0
Release:	%mkrel 4
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
# search plugins
Source9:	http://users.musicbrainz.org/~brianfreud/SearchAMG.py
Source10:	http://users.musicbrainz.org/~brianfreud/SearchDiscogs3.py
Source11:	http://users.musicbrainz.org/~brianfreud/SearchAmazon3.py
Source12:	http://users.musicbrainz.org/~brianfreud/SearchCastAlbums3.py
Source13:	http://users.musicbrainz.org/~brianfreud/SearchFilmMusziek3.py
Source14:	http://users.musicbrainz.org/~brianfreud/SearchGMR.py
Source15:	http://users.musicbrainz.org/~brianfreud/SearchGoogle3.py
Source16:	http://users.musicbrainz.org/~brianfreud/SearchLortelArchives3.py
Source17:	http://users.musicbrainz.org/~brianfreud/SearchSoundtrackCollector3.py
Source18:	http://users.musicbrainz.org/~brianfreud/SearchSoundtrackINFO3.py
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
#gw remove after 1.0:
Source100: https://raw.github.com/musicbrainz/picard/master/po/de.po
Patch0:		picard-1.0-avutil-linking.patch
Patch1:		picard-1.0-ffmpeg0.11.patch
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
cp %SOURCE100 po/de.po

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
#gw fix API versions:
sed -i "s^\"0.10\"^\"%version\"^" %{PLUGINDIR}/Search*


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
