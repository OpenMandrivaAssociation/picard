Summary:	The official MusicBrainz tagger
Name:		picard
Version:	2.13.2
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://picard.musicbrainz.org/
Source0:	https://data.musicbrainz.org/pub/musicbrainz/%name/%name-%version.tar.gz

BuildSystem:    python

BuildRequires:	mutagen
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:  pkgconfig(python)
BuildRequires:  gettext
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

%files 
%doc AUTHORS.txt 
%license COPYING.txt
%{_bindir}/%{name}
%{_datadir}/locale/
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python_sitearch}/*
%{_iconsdir}/hicolor/*/apps/*
