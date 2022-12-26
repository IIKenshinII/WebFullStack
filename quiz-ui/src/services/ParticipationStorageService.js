export default {
  clear() {
    // todo : implement
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    // todo : implement
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    // todo : implement
    window.localStorage.setItem("participationScore", JSON.stringify(participationScore));
  },
  getParticipationScore() {
    // todo : implement
    return JSON.parse(window.localStorage.getItem("participationScore"));
  }
};