<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<script>
import _ from "lodash";
export default {
  name: "App",
  data() {
    return {
      // num : -5,
      // display : false,
      // showElement: false,
      names: ['Bruce', 'Clark','Diana','Barry'],
      // fullnames : [
      //   { first: 'Bruce', last: 'Wayne'},
      //   { first: 'Clark', last: 'Kent'},
      //   { first: 'Princess', last: 'Diana'},
      // ],
      // actors: [
      //   {
      //     name: 'Chirstan Bale',
      //     movies: ['Demacia','The Final Season'],
      //   },
      //   {
      //     name: 'Di Caprios',
      //     movies: ['The Last Season', 'Titanic'],
      //   },
      };
    },
    methods: {
      shuffle() {
        console.log(this.names);
        this.names = _.shuffle(this.names);
      }
    }
}
</script>

<template>
  <main>
    <!-- <h2 v-if="num === 0"> The number is zero </h2> -->
    <!-- <h2 v-else-if="num < 0"> The number is negative</h2>
    <h2 v-else-if="num > 0"> The number is positive</h2>
    <h2 v-else> It is not a number</h2> -->
    <template v-for="name in names" :key="name">
    <h2> {{ name }}</h2>
    <input placeholder="Last name">
    <hr />
  </template>
  <button @click="shuffle">Shuffle!</button>
    <!-- <hr />
    <h2 v-if="display" v-for="(name, index) in names" :key ="name">{{ index }} {{ name }}</h2>
    <hr />
    <h2 v-if="display" v-for="(name, index) in fullnames" :key ="name.first">{{ name.first }} {{ name.last }}</h2>
    <hr />
    <div v-for="actor in actors" :key ="actor.name" v-if="display">
      <br>
      <h2>{{ actor.name }}</h2>
      <h3 v-for="movie in actor.movies" :key="movie">{{ movie }}</h3>
    </div>
    <hr />
  <template v-if="display">
    <h2> MinhHoang</h2>
    <h2> Code</h2>
    <h2> Vue </h2>
  </template>
  <h2 v-show="showElement"> Using v-show</h2>
  <h2 v-if="showElement">Using v-if</h2> -->
  </main> 

</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
