<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-4">

    <!-- Toast Notification -->
    <transition name="toast">
      <div
        v-if="toast.show"
        class="fixed top-4 left-1/2 -translate-x-1/2 z-50 px-6 py-3 rounded-xl shadow-lg backdrop-blur-lg bg-red-500/90 text-white font-medium"
      >
        {{ toast.message }}
      </div>
    </transition>

    <!-- Loading State -->
    <div v-if="loading" class="text-white text-xl">
      <svg class="animate-spin h-8 w-8 mx-auto mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      Loading poll...
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-white/10 backdrop-blur-lg rounded-2xl p-8 text-center max-w-md w-full">
      <div class="text-red-200 text-6xl mb-4">:(</div>
      <h2 class="text-white text-xl font-semibold mb-2">Poll Not Found</h2>
      <p class="text-white/70">{{ error }}</p>
    </div>

    <!-- Poll Content -->
    <div v-else class="w-full max-w-lg">

      <!-- Voting View -->
      <transition name="fade" mode="out-in">
        <div v-if="!hasVoted && !showResults" key="voting" class="bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-2xl">
          <h1 class="text-white text-2xl font-bold text-center mb-6 leading-tight">{{ poll.question }}</h1>

          <p v-if="poll.description" class="text-white/70 text-center mb-6 text-sm">{{ poll.description }}</p>

          <div class="space-y-3">
            <button
              v-for="answer in poll.answers"
              :key="answer.id"
              @click="selectAnswer(answer.id)"
              :class="[
                'w-full p-4 rounded-xl text-left transition-all duration-200 transform active:scale-[0.98]',
                selectedAnswer === answer.id
                  ? 'bg-white text-purple-600 shadow-lg scale-[1.02]'
                  : 'bg-white/20 text-white hover:bg-white/30'
              ]"
            >
              <span class="font-medium">{{ answer.text }}</span>
            </button>
          </div>

          <button
            @click="submitVote"
            :disabled="!selectedAnswer || submitting"
            :class="[
              'w-full mt-6 py-4 rounded-xl font-semibold text-lg transition-all duration-200',
              selectedAnswer && !submitting
                ? 'bg-white text-purple-600 shadow-lg active:scale-[0.98]'
                : 'bg-white/30 text-white/50 cursor-not-allowed'
            ]"
          >
            <span v-if="submitting">
              <svg class="animate-spin h-5 w-5 inline mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Submitting...
            </span>
            <span v-else>Vote</span>
          </button>
        </div>

        <!-- Results View -->
        <div v-else key="results" class="bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-2xl">
          <div class="text-center mb-6">
            <div class="text-4xl mb-2">&#127881;</div>
            <h2 class="text-white text-xl font-bold">{{ hasVoted ? 'Thanks for voting!' : 'Results' }}</h2>
          </div>

          <h1 class="text-white text-xl font-semibold text-center mb-6">{{ poll.question }}</h1>

          <div class="space-y-4">
            <div v-for="answer in sortedAnswers" :key="answer.id" class="relative">
              <div class="flex justify-between items-center mb-1">
                <span class="text-white font-medium text-sm truncate pr-2">{{ answer.text }}</span>
                <span class="text-white/80 text-sm whitespace-nowrap">{{ answer.votes_count }} vote{{ answer.votes_count !== 1 ? 's' : '' }}</span>
              </div>
              <div class="h-10 bg-white/20 rounded-lg overflow-hidden relative">
                <div
                  class="h-full rounded-lg bar-animate flex items-center justify-end pr-3"
                  :class="answer.id === votedAnswerId ? 'bg-gradient-to-r from-green-400 to-emerald-500' : 'bg-gradient-to-r from-white/40 to-white/60'"
                  :style="{ width: getPercentage(answer.votes_count) + '%' }"
                >
                  <span v-if="getPercentage(answer.votes_count) > 10" class="text-sm font-bold" :class="answer.id === votedAnswerId ? 'text-white' : 'text-purple-700'">
                    {{ getPercentage(answer.votes_count).toFixed(0) }}%
                  </span>
                </div>
                <span v-if="getPercentage(answer.votes_count) <= 10" class="absolute right-3 top-1/2 -translate-y-1/2 text-sm font-bold text-white/80">
                  {{ getPercentage(answer.votes_count).toFixed(0) }}%
                </span>
              </div>
            </div>
          </div>

          <div class="mt-6 pt-4 border-t border-white/20 text-center">
            <p class="text-white/60 text-sm">Total votes: {{ totalVotes }}</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Poll',
  data() {
    return {
      pollId: null,
      poll: null,
      loading: true,
      error: null,
      selectedAnswer: null,
      submitting: false,
      hasVoted: false,
      showResults: false,
      votedAnswerId: null,
      toast: {
        show: false,
        message: ''
      }
    };
  },
  computed: {
    totalVotes() {
      if (!this.poll || !this.poll.answers) return 0;
      return this.poll.answers.reduce((sum, a) => sum + a.votes_count, 0);
    },
    sortedAnswers() {
      if (!this.poll || !this.poll.answers) return [];
      return [...this.poll.answers].sort((a, b) => b.votes_count - a.votes_count);
    }
  },
  methods: {
    getPollIdFromUrl() {
      const path = window.location.pathname;
      const match = path.match(/\/polls\/(\d+)/);
      return match ? parseInt(match[1]) : null;
    },
    getVoterId() {
      let voterId = localStorage.getItem('poll_voter_id');
      if (!voterId) {
        voterId = 'voter_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('poll_voter_id', voterId);
      }
      return voterId;
    },
    hasVotedOnPoll(pollId) {
      const votedPolls = JSON.parse(localStorage.getItem('voted_polls') || '{}');
      return votedPolls[pollId] !== undefined;
    },
    getVotedAnswerId(pollId) {
      const votedPolls = JSON.parse(localStorage.getItem('voted_polls') || '{}');
      return votedPolls[pollId] || null;
    },
    markAsVoted(pollId, answerId) {
      const votedPolls = JSON.parse(localStorage.getItem('voted_polls') || '{}');
      votedPolls[pollId] = answerId;
      localStorage.setItem('voted_polls', JSON.stringify(votedPolls));
    },
    async fetchPoll() {
      try {
        const response = await fetch(`/api/v1/polls/${this.pollId}`);
        const data = await response.json();

        if (!data.success) {
          this.error = data.message || 'Failed to load poll';
          return;
        }

        this.poll = data.poll;
      } catch (err) {
        this.error = 'Failed to connect to server';
      } finally {
        this.loading = false;
      }
    },
    selectAnswer(answerId) {
      this.selectedAnswer = answerId;
    },
    async submitVote() {
      if (!this.selectedAnswer || this.submitting) return;

      this.submitting = true;

      try {
        const response = await fetch(`/api/v1/polls/${this.pollId}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            answer_id: this.selectedAnswer,
            voter_identifier: this.getVoterId()
          })
        });

        const data = await response.json();

        if (data.success) {
          this.markAsVoted(this.pollId, this.selectedAnswer);
          this.votedAnswerId = this.selectedAnswer;
          this.poll = data.poll;
          this.hasVoted = true;
          this.showResults = true;
        } else if (data.already_voted) {
          this.showToast(data.message);
          this.poll = data.poll;
          this.showResults = true;
        } else {
          this.showToast(data.message || 'Failed to submit vote');
        }
      } catch (err) {
        this.showToast('Failed to submit vote. Please try again.');
      } finally {
        this.submitting = false;
      }
    },
    getPercentage(votes) {
      if (this.totalVotes === 0) return 0;
      return (votes / this.totalVotes) * 100;
    },
    showToast(message) {
      this.toast.message = message;
      this.toast.show = true;
      setTimeout(() => {
        this.toast.show = false;
      }, 3000);
    }
  },
  async mounted() {
    this.pollId = this.getPollIdFromUrl();

    if (!this.pollId) {
      this.error = 'Invalid poll URL';
      this.loading = false;
      return;
    }

    if (this.hasVotedOnPoll(this.pollId)) {
      this.hasVoted = true;
      this.showResults = true;
      this.votedAnswerId = this.getVotedAnswerId(this.pollId);
    }

    await this.fetchPoll();
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.slide-enter-active, .slide-leave-active {
  transition: all 0.5s ease;
}
.slide-enter-from {
  transform: translateX(100%);
  opacity: 0;
}
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
.bar-animate {
  transition: width 0.8s ease-out;
}
.toast-enter-active {
  transition: all 0.3s ease-out;
}
.toast-leave-active {
  transition: all 0.3s ease-in;
}
.toast-enter-from {
  transform: translate(-50%, -100%);
  opacity: 0;
}
.toast-leave-to {
  transform: translate(-50%, -20px);
  opacity: 0;
}
</style>
