let xgChartInstance = null;
let xPTSChartInstance = null;

document.addEventListener('DOMContentLoaded', function() {
  const leagueName = getLeagueNameFromURL();
  const initialSeason = getSeasonFromURL() || '2022';
  populateSeasons(initialSeason);
  updateLeagueTable(leagueName, initialSeason);
  setLeagueInfo(leagueName);


    const path = window.location.pathname;

    const navLinks = document.querySelectorAll('header nav ul li a, footer ul li a, .dropdown-content a');

    navLinks.forEach(function(link) {
        if (link.href.endsWith(path)) { //   it matches the end of the path
            // Add the active-link class to the link
            link.classList.add('active-link');
            if (link.closest('.dropdown-content')) {
                link.closest('.dropdown').querySelector('a').classList.add('active-link');
            }
        }
    });
});

function formatLeagueNameForPath(leagueNameFromURL) {
  return leagueNameFromURL.replace('_', '').toLowerCase();
}


function updateURLPath(leagueName, selectedSeason) {
  // Construct the new URL path
  const newPath = `/leagues/${encodeURIComponent(leagueName)}/${encodeURIComponent(selectedSeason)}/`;
  window.history.pushState({ path: newPath }, '', newPath);
}

function setLeagueInfo(leagueName) {
  const formattedLeagueName = formatLeagueNameForPath(leagueName);

  const leagueDisplayNameMap = {
      'epl': 'English Premier League',
      'bundesliga': 'Bundesliga',
      'laliga': 'La Liga',
      'ligue1': 'Ligue 1',
      'seriea': 'Serie A'
  };

  const leagueLogoElement = document.getElementById('league-logo');
  leagueLogoElement.src = leagueLogoPaths[formattedLeagueName];
  leagueLogoElement.alt = leagueDisplayNameMap[formattedLeagueName] + ' Logo';

  const leagueNameElement = document.getElementById('league-name');
  leagueNameElement.textContent = leagueDisplayNameMap[formattedLeagueName];
}


function getLeagueNameFromURL() {
  const pathParts = window.location.pathname.split('/').filter(Boolean);
  return pathParts[1];
}

function getSeasonFromURL() {
  const pathParts = window.location.pathname.split('/').filter(Boolean);
  return pathParts[2];
}

function populateSeasons(selectedSeason) {
  const seasons = [];
  for (let year = 2014; year <= new Date().getFullYear(); year++) {
    seasons.push(year.toString());
  }

  const seasonSelect = document.getElementById('season-select');
  seasons.forEach(season => {
    const option = document.createElement('option');
    option.value = season;
    option.textContent = season;
    option.selected = season === selectedSeason;
    seasonSelect.appendChild(option);
  });

  seasonSelect.addEventListener('change', function(event) {
    const leagueName = getLeagueNameFromURL();
    const selectedSeason = event.target.value;
    updateLeagueTable(leagueName, selectedSeason);
    updateURLPath(leagueName, selectedSeason);
  });
}

function updateLeagueTable(leagueName, season) {
  fetch(`/leagues/api/leagues/${encodeURIComponent(leagueName)}/${season}/`)
    .then(response => response.json())
    .then(clubsData => {
      const tableBody = document.getElementById('league-table').querySelector('tbody');
      tableBody.innerHTML = '';

      const seasonTotals = clubsData.map(club => {
        // Split the title into parts
        const parts = club.title.split('_');
        // Determine the starting index for the club name
        const startIndex = leagueName.includes('_') ? 3 : 2; // Adjusted index based on league name
        // Join the remaining parts back together to form the club name
        const clubName = parts.slice(startIndex).join(' ');

        // Exclude clubs where the name ends with "2"
        if (clubName.endsWith(" 2")) {
          return null;
        }


        
        

        // Accumulate the season totals for each club
        const totals = club.data.reduce((acc, match) => {
          acc.pts += match.pts;
          acc.scored += match.scored;
          acc.wins += match.result === 'w' ? 1 : 0;
          acc.draws += match.result === 'd' ? 1 : 0;
          acc.loses += match.result === 'l' ? 1 : 0;
          acc.total_xG += match.xg;
          acc.total_xPTS += match.xpts;
          return acc;
        }, { pts: 0, scored: 0, wins: 0, draws: 0, loses: 0, total_xG: 0, total_xPTS: 0 });

        // Return the accumulated totals along with the club name
        return totals ? { ...totals, club: clubName } : null;
      }).filter(totals => totals !== null); // Filter out the null entri

      // Sort the clubs by points in descending order
      seasonTotals.sort((a, b) => b.pts - a.pts);

      // Populate the table with sorted season totals
      seasonTotals.forEach((totals, index) => {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = index + 1;
        row.insertCell(1).textContent = totals.club;
        row.insertCell(2).textContent = totals.total_xG.toFixed(2);
        row.insertCell(3).textContent = totals.total_xPTS.toFixed(2);
        row.insertCell(4).textContent = totals.scored;
        row.insertCell(5).textContent = totals.wins;
        row.insertCell(6).textContent = totals.draws;
        row.insertCell(7).textContent = totals.loses;
        row.insertCell(8).textContent = totals.pts;
      });

    updateCharts(seasonTotals);
    })
    .catch(error => {
      console.error('Error fetching league table:', error);
    });
}


function updateCharts(seasonTotals) {
  if (xgChartInstance) {
    xgChartInstance.destroy();
  }
  if (xPTSChartInstance) {
    xPTSChartInstance.destroy();
  }

  const xGData = seasonTotals.map(totals => ({ label: totals.club, xG: totals.total_xG }));
  xGData.sort((a, b) => b.xG - a.xG);

  const xPTSData = seasonTotals.map(totals => ({ label: totals.club, xPTS: totals.total_xPTS }));
  xPTSData.sort((a, b) => b.xPTS - a.xPTS);

  const xgCtx = document.getElementById('xg-chart').getContext('2d');
  xgChartInstance = new Chart(xgCtx, {
    type: 'bar',
    data: {
      labels: xGData.map(item => item.label),
      datasets: [{
        label: 'Total xG',
        data: xGData.map(item => item.xG),
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    },
    options: { scales: { y: { beginAtZero: true } } }
  });

  const xPTSctx = document.getElementById('xpts-chart').getContext('2d');
  xPTSChartInstance = new Chart(xPTSctx, {
    type: 'line',
    data: {
      labels: xPTSData.map(item => item.label),
      datasets: [{
        label: 'Total xPTS',
        data: xPTSData.map(item => item.xPTS),
        fill: false,
        borderColor: 'rgba(54, 162, 235, 1)',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderWidth: 2
      }]
    },
    options: { scales: { y: { beginAtZero: true } } }
  });
}

