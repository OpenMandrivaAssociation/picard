Summary:	The official MusicBrainz tagger
Name:		picard
Version:	2.9
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://picard.musicbrainz.org/
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz
# Plugins:
Source1:	http://users.musicbrainz.org/~luks/picard-plugins/classicdiscnumber.py
Source2:	http://users.musicbrainz.org/~luks/picard-plugins/coverart.py
Source3:	http://users.musicbrainz.org/~luks/picard-plugins/cuesheet.py
Source4:	http://users.musicbrainz.org/~luks/picard-plugins/discnumber.py
Source5:	http://users.musicbrainz.org/~luks/picard-plugins/featartist.py
Source6:	http://users.musicbrainz.org/~luks/picard-plugins/open_in_gui.py
Source7:	http://users.musicbrainz.org/~luks/picard-plugins/swapprefix.py
Source8:	http://users.musicbrainz.org/~luks/picard-plugins/titlecase.py
Source9:	http://users.musicbrainz.org/~luks/picard-plugins/tracks2clipboard.py
# replaygain plugin
Source13:	http://users.musicbrainz.org/~luks/picard-plugins/replaygain/__init__.py
Source14:	http://users.musicbrainz.org/~luks/picard-plugins/replaygain/options_replaygain.ui
Source15:	http://users.musicbrainz.org/~luks/picard-plugins/replaygain/ui_options_replaygain.py
Source16:	http://gitorious.org/musicbrainz/addrelease/blobs/raw/master/addrelease.py
Source17:	http://users.musicbrainz.org/~luks/picard-plugins/release_type.py
Source18:	http://users.musicbrainz.org/~luks/picard-plugins/featartistsintitles.py
Source19:	http://users.musicbrainz.org/~luks/picard-plugins/no_release.py
Source20:	http://github.com/voiceinsideyou/creaps-picard-plugins/raw/master/titleversion.py
Source21:	http://github.com/voiceinsideyou/creaps-picard-plugins/raw/master/titlesort.py
Source22:	https://github.com/voiceinsideyou/picard/raw/plugins/contrib/plugins/removeperfectalbums.py
Source23:	https://raw.github.com/encukou/picard-plugins/master/autosave.py
# https://musicbrainz.org/doc/MusicBrainz_Picard/Documentation/Plugins/Lastfmplus
Source24:	https://picard.musicbrainz.org/api/v2/download?id=lastfm#/lastfm.zip
# search plugins https://github.com/brianfreud/Picard-plugins
Source25:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchAMG.py
Source26:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchDiscogs3.py
Source27:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchAmazon3.py
Source28:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchCastAlbums3.py
Source29:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchFilmMusziek3.py
Source30:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchGMR.py
Source31:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchGoogle3.py
Source32:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchLortelArchives3.py
Source33:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchSoundtrackCollector3.py
Source34:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchSoundtrackINFO3.py
Source35:	https://raw.github.com/brianfreud/Picard-plugins/master/SearchEbay.py

BuildRequires:	mutagen
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libdiscid)
Requires:	mutagen
Requires:	%{mklibname discid 0}
#gw for fpcalc (AcoustID calculation)
Requires:	chromaprint
#gw for metaflac:
Suggests:	flac
#gw for wvgain:
Suggests:	wavpack
Suggests:	mp3gain

%description
MusicBrainz Picard is the official MusicBrainz tagger, written in Python.

Picard supports the majority of audio file formats, is capable of using audio
fingerprints (PUIDs), performing CD lookups and disc ID submissions, and it has
excellent Unicode support. Additionally, there are several plugins available
that extend Picard's features.

When tagging files, Picard uses an album-oriented approach. This approach
allows it to utilize the MusicBrainz data as effectively as possible and
correctly tag your music. For more information, see the illustrated quick start
guide to tagging.

Picard is named after Captain Jean-Luc Picard from the TV series Star Trek: The
Next Generation.

%prep
%autosetup -p1 -n %{name}-release-%{version}
python setup.py config

%build
%py_build

%install
%py_install

PLUGINDIR=%{buildroot}%{python_sitearch}/picard/plugins/
install -m 0644 %{SOURCE1} ${PLUGINDIR}
install -m 0644 %{SOURCE2} ${PLUGINDIR}
install -m 0644 %{SOURCE3} ${PLUGINDIR}
install -m 0644 %{SOURCE4} ${PLUGINDIR}
install -m 0644 %{SOURCE5} ${PLUGINDIR}
install -m 0644 %{SOURCE6} ${PLUGINDIR}
install -m 0644 %{SOURCE7} ${PLUGINDIR}
install -m 0644 %{SOURCE8} ${PLUGINDIR}
install -m 0644 %{SOURCE9} ${PLUGINDIR}
mkdir -p ${PLUGINDIR}/replaygain
install -m 0644 %{SOURCE13} ${PLUGINDIR}/replaygain/__init__.py
install -m 0644 %{SOURCE14} ${PLUGINDIR}/replaygain/
install -m 0644 %{SOURCE15} ${PLUGINDIR}/replaygain/
install -m 0644 %{SOURCE16} ${PLUGINDIR}
install -m 0644 %{SOURCE17} ${PLUGINDIR}
install -m 0644 %{SOURCE18} ${PLUGINDIR}
install -m 0644 %{SOURCE19} ${PLUGINDIR}
install -m 0644 %{SOURCE20} ${PLUGINDIR}
install -m 0644 %{SOURCE21} ${PLUGINDIR}
install -m 0644 %{SOURCE22} ${PLUGINDIR}
install -m 0644 %{SOURCE23} ${PLUGINDIR}
unzip %{SOURCE24} -d ${PLUGINDIR}
install -m 0644 %{SOURCE25} ${PLUGINDIR}
install -m 0644 %{SOURCE26} ${PLUGINDIR}
install -m 0644 %{SOURCE27} ${PLUGINDIR}
install -m 0644 %{SOURCE28} ${PLUGINDIR}
install -m 0644 %{SOURCE29} ${PLUGINDIR}
install -m 0644 %{SOURCE30} ${PLUGINDIR}
install -m 0644 %{SOURCE31} ${PLUGINDIR}
install -m 0644 %{SOURCE32} ${PLUGINDIR}
install -m 0644 %{SOURCE33} ${PLUGINDIR}
install -m 0644 %{SOURCE34} ${PLUGINDIR}
install -m 0644 %{SOURCE35} ${PLUGINDIR}

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS.txt COPYING.txt
%{_bindir}/%{name}
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python_sitearch}/*
%{_iconsdir}/hicolor/*/apps/*
