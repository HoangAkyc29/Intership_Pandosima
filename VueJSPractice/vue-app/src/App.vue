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
      count: 0,
      firstName: 'Diana',
      lastName: 'Barry',
      items: [
        {
          id: 1,
          title: 'TV',
          price: 100,
        },
        {
          id: 2,
          title: 'Phone',
          price: 200,
        },
        {
          id: 3,
          title: 'Computer',
          price: 250,
        }
      ],
      formValues: {
        name: '',
        profileSummary: '',
        conutry: '',
        jobLocation: [],
        Workremote: "no",
        Skillset: [],
      }
    }
    },
    computed: {
      fullname() {
          return `${this.firstName} ${this.lastName}`
      },
      total() {
        return this.items.reduce((total, curr) => (total = total + curr.price), 0)
      }
    },
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
    methods: {
      shuffle() {
        console.log(this.names);
        this.names = _.shuffle(this.names);
      },
      increasement(num) {
        this.count += num;
      },
      changeName(event) {
        this.names = ['Bruce2', 'Clark2','Diana2','Barry2']
        console.log('Event: ' + event);
      },
      submitForm(event) {
        event.preventDefault()
        console.log('Form values: ' + this.formValues);
      }
    }
}
</script>

<template>
  <!-- <main>
     <h2 v-if="num === 0"> The number is zero </h2> -->
    <!-- <h2 v-else-if="num < 0"> The number is negative</h2>
    <h2 v-else-if="num > 0"> The number is positive</h2>
    <h2 v-else> It is not a number</h2> -->
    <!-- <template v-for="name in names" :key="name">
    <h2> {{ name }}</h2>
    <input placeholder="Last name">
    <hr />
  </template>
  <button @click="shuffle">Shuffle!</button> -->
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
  <h2 v-if="showElement">Using v-if</h2> 
  </main> -->
  <!-- <main>
    <h2 v-for="(name, index) in names" :key ="name">{{ index }} {{ name }}</h2>
    <div>
       <button @click="names = ['Bruce2', 'Clark2']"> Change name</button>
      <button @click="changeName($event), increasement(1)"> Change name</button>
    </div>
    <h2> {{ count }}</h2>
    <div>
      <button v-on:click="increasement(5)"> Count Increase</button>
      <button v-on:click="count -= 1"> Count Decrease</button>
    </div>
    <h2> FullName - {{ firstName }} {{ lastName }}</h2>
    <h2> Computed fullname - {{ fullname }}</h2>
    <button @click= "items.push({id:4, title:'Keyboard',price:50})"> Add Item </button>
    <h2> Computed Total - {{ total }}</h2>
  </main> -->
  <main justify-content="center">
    <div>
    <pre>
      {{ JSON.stringify(formValues, null, 2)}}
    </pre>
  </div>
  <form @submit="submitForm">
    <div>
      <label for="name">Name</label>
      <br/>
      <input type="text" id ="name" v-model="formValues.name" />
    </div>
    <div>
      <label for="profile">Profile Summary</label>
      <br/>
      <textarea type="text" id ="profile" v-model="formValues.profileSummary" />
    </div>

    <div>
      <label for="country">Country</label>
      <br/>
      <select id="country" v-model="formValues.conutry">
        <option value=""> Select a country</option>
        <option value="India"> India</option>
        <option value="Vietnam"> Vietnam</option>
        <option value="Singapore"> Singapore</option>
      </select>
    </div>

    <div>
      <label for="jobLocation">Job Location</label>
      <br/>
      <select id="jobLocation" multiple v-model="formValues.jobLocation">
        <option value=""> Select a country</option>
        <option value="India"> India</option>
        <option value="Vietnam"> Vietnam</option>
        <option value="Singapore"> Singapore</option>
        <option value="Jujutsu"> Jujutsu </option>
      </select>
    </div>

    <div>
      <input type="checkbox" id="Workremote" v-model="formValues.Workremote" true-value="yes" false-value="no"/>
      <label for="Workremote"> Open to remote Work ?</label> 
    </div>

    <div>
      <input type="checkbox" id="html" value="html" v-model="formValues.Skillset">
      <label for="html"> HTML </label>
      <input type="checkbox" id="css" value="css" v-model="formValues.Skillset">
      <label for="css"> CSS </label>
      <input type="checkbox" id="typescript" value="typescript" v-model="formValues.Skillset">
      <label for="typescript"> TYPESCRIPT </label>
    </div>
    <div>
      <button>Submit</button>
    </div>
  </form>
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
