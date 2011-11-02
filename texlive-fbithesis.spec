Name:		texlive-fbithesis
Version:	1.2m
Release:	1
Summary:	Computer Science thesis class for University of Dortmund
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fbithesis
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbithesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
At the department of computer science at the University of
Dortmund there are cardboard cover pages for research or
internal reports like master/phd-theses. The main function of
this LaTeX2e document-class is a replacement for the \maketitle
command to typeset a title page that is adjusted to these cover
pages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fbithesis/fbithesis.cfg
%{_texmfdistdir}/tex/latex/fbithesis/fbithesis.cls
%doc %{_texmfdistdir}/doc/latex/fbithesis/README
%doc %{_texmfdistdir}/doc/latex/fbithesis/distribution.key
%doc %{_texmfdistdir}/doc/latex/fbithesis/example.pdf
%doc %{_texmfdistdir}/doc/latex/fbithesis/example.tex
%doc %{_texmfdistdir}/doc/latex/fbithesis/exampleaux.tex
%doc %{_texmfdistdir}/doc/latex/fbithesis/fbithesis.dtx.asc
%doc %{_texmfdistdir}/doc/latex/fbithesis/fbithesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fbithesis/fbithesis.drv
%doc %{_texmfdistdir}/source/latex/fbithesis/fbithesis.dtx
%doc %{_texmfdistdir}/source/latex/fbithesis/fbithesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
