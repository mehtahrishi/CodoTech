document.addEventListener('DOMContentLoaded', () => {
    // --- STATE MANAGEMENT ---
    const songLibrary = window.SONG_LIBRARY || []; 
    const interestedArtists = new Set();
    const listenedTrackIds = new Set();
    let lastClickedArtist = null;
    let currentPlayingTrackItem = null;
    let currentPlaylist = []; // This will hold the active playlist (Library or Recommendations)

    // --- DOM ELEMENT SELECTORS ---
    const getRecsBtn = document.getElementById('get-recs-btn');
    const recommendationList = document.getElementById('recommendation-list');
    const libraryList = document.getElementById('trending-list');
    
    const playerTrackName = document.getElementById('player-track-name');
    const playerArtistName = document.getElementById('player-artist-name');
    const playerAlbumArt = document.getElementById('player-album-art');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    const audioPreview = document.getElementById('audio-preview');
    const progressBar = document.getElementById('progress-bar');
    const progressBarContainer = document.querySelector('.progress-bar-container');

    // --- CORE FUNCTIONS ---

    const renderTrackList = (container, tracks) => {
        container.innerHTML = '';
        if (!tracks || tracks.length === 0) {
            container.innerHTML = `<li class="placeholder">No new recommendations. Listen to more artists!</li>`;
            return;
        }

        tracks.forEach(track => {
            const li = document.createElement('li');
            li.className = 'track-item';
            // Use our own consistent keys from the song library
            li.dataset.trackId = track.track_id || track.id;
            li.dataset.trackName = track.track_name || track.name;
            li.dataset.artistName = track.artist_name || track.artist;
            li.dataset.previewUrl = track.cloudinary_url || track.preview_url || '';
            li.dataset.albumArt = track.album_art_url || track.album_art || '/static/img/placeholder.png';

            li.innerHTML = `
                <img src="${li.dataset.albumArt}" class="track-album-art" alt="album art">
                <div class="track-details">
                    <span class="track-name">${li.dataset.trackName}</span>
                    <span class="artist-name">${li.dataset.artistName}</span>
                </div>`;
            container.appendChild(li);
        });
    };
    
    const generateRecommendations = () => {
        // ... (This logic is already correct and doesn't need to change)
        if (interestedArtists.size === 0) { renderTrackList(recommendationList, []); return; }
        const songsByLastArtist = songLibrary.filter(track => track.artist_name === lastClickedArtist);
        if (songsByLastArtist.length <= 1) {
            const otherArtists = {};
            songLibrary.forEach(track => {
                if (track.artist_name !== lastClickedArtist) {
                    if (!otherArtists[track.artist_name]) otherArtists[track.artist_name] = [];
                    otherArtists[track.artist_name].push(track);
                }
            });
            const discoveryMix = Object.values(otherArtists).map(artistTracks => artistTracks[Math.floor(Math.random() * artistTracks.length)]);
            renderTrackList(recommendationList, discoveryMix);
            return;
        }
        let potentialRecs = songLibrary.filter(track => interestedArtists.has(track.artist_name));
        let finalRecs = potentialRecs.filter(track => !listenedTrackIds.has(track.track_id));
        renderTrackList(recommendationList, finalRecs);
    };


    // --- PLAYER & EVENT HANDLERS ---

    const playTrack = (trackItem) => {
        if (!trackItem) return;
        
        const trackData = trackItem.dataset;

        if (trackData.previewUrl) {
            updatePlayerUI(trackData);
            audioPreview.src = trackData.previewUrl;
            audioPreview.play();
            highlightPlayingTrack(trackItem);
            currentPlayingTrackItem = trackItem;
        } else {
            // Fallback for tracks without audio
            updatePlayerUI(trackData);
        }
    };

    const handleTrackClick = (trackItem) => {
        const trackData = trackItem.dataset;
        
        // This is a crucial fix: Determine which playlist was clicked
        if(trackItem.closest('#trending-list')){
            currentPlaylist = Array.from(libraryList.querySelectorAll('.track-item'));
        } else {
            currentPlaylist = Array.from(recommendationList.querySelectorAll('.track-item'));
        }

        // Add to interest list and log the listen
        interestedArtists.add(trackData.artistName);
        listenedTrackIds.add(trackData.trackId);
        lastClickedArtist = trackData.artistName;

        playTrack(trackItem);
    };

    const handleNext = () => {
        if (!currentPlayingTrackItem || currentPlaylist.length === 0) return;
        
        const currentIndex = currentPlaylist.findIndex(item => item === currentPlayingTrackItem);
        const nextIndex = (currentIndex + 1) % currentPlaylist.length; // Loop back to the start
        playTrack(currentPlaylist[nextIndex]);
    };

    const handlePrev = () => {
        if (!currentPlayingTrackItem || currentPlaylist.length === 0) return;
        
        const currentIndex = currentPlaylist.findIndex(item => item === currentPlayingTrackItem);
        const prevIndex = (currentIndex - 1 + currentPlaylist.length) % currentPlaylist.length; // Loop back to the end
        playTrack(currentPlaylist[prevIndex]);
    };

    const updateProgressBar = () => {
        if (audioPreview.duration) {
            const progressPercent = (audioPreview.currentTime / audioPreview.duration) * 100;
            progressBar.style.width = `${progressPercent}%`;
        }
    };
    
    const seek = (e) => {
        const width = progressBarContainer.clientWidth;
        const clickX = e.offsetX;
        if(audioPreview.duration){
            audioPreview.currentTime = (clickX / width) * audioPreview.duration;
        }
    };

    // --- UI & INITIALIZATION ---

    const updatePlayerUI = (trackData) => {
        playerTrackName.textContent = trackData.trackName;
        playerArtistName.textContent = trackData.artistName;
        playerAlbumArt.src = trackData.albumArt;
    };

    const highlightPlayingTrack = (trackItem) => {
        document.querySelectorAll('.track-item.playing').forEach(item => item.classList.remove('playing'));
        if (trackItem) trackItem.classList.add('playing');
    };

    // Initial setup
    getRecsBtn.addEventListener('click', generateRecommendations);
    document.body.addEventListener('click', (event) => {
        const trackItem = event.target.closest('.track-item');
        if (trackItem) handleTrackClick(trackItem);
    });
    
    // Player controls listeners
    playPauseBtn.addEventListener('click', () => {
        if (audioPreview.src) audioPreview.paused ? audioPreview.play() : audioPreview.pause();
    });
    nextBtn.addEventListener('click', handleNext);
    prevBtn.addEventListener('click', handlePrev);
    
    // Progress bar listeners
    audioPreview.addEventListener('timeupdate', updateProgressBar);
    audioPreview.addEventListener('ended', handleNext); // Automatically play next song
    progressBarContainer.addEventListener('click', seek);

    audioPreview.addEventListener('play', () => playPauseBtn.textContent = '⏸️');
    audioPreview.addEventListener('pause', () => playPauseBtn.textContent = '▶️');
    
    // Populate the main song library on page load
    renderTrackList(libraryList, songLibrary);
    getRecsBtn.innerHTML = '<span class="btn-text">Get Recommendations</span><div class="spinner"></div>';
});
