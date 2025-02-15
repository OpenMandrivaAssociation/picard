# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%global commit_tag 14005d0429f807247d085f630aa73372dc43a13d

Summary:	      The official MusicBrainz tagger
Name:		       picard
Version:	      3.0.0
# When using a commit_tag (i.e. not %{nil}) add a commit date 
# decoration ~0.yyyyMMdd. to Release number
Release:	      ~0.20250214.1
License:	      GPLv2+
Group:		      Sound
Url:		        https://picard.musicbrainz.org/
#Source0:	      https://data.musicbrainz.org/pub/musicbrainz/%name/%name-%version.tar.gz
# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        https://github.com/metabrainz/picard/archive/%{commit_tag}.tar.gz#/%name-%version.%release.tar.gz
%else
Source0:        https://github.com/<org_name>/<project_name>/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildSystem:    python

BuildRequires:	mutagen
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:  pkgconfig(python)
BuildRequires:  gettext

Requires:       %{_lib}xcb-cursor0
Requires:	     mutagen
Requires:       python-fasteners
Requires:       python-markdown
Requires:       python-pyjwt 
Requires:       python-libdiscid
Requires:       python-dateutil 
Requires:       python-pyyaml
Requires:       python-qt6
Requires:	     %{mklibname discid 0}
#gw for fpcalc (AcoustID calculation)
Recommends:	     chromaprint
#gw for metaflac:
Suggests:	     flac
#gw for wvgain:
Suggests:	     wavpack
Suggests:	     mp3gain

AutoReq:        no

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
