<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<script>
export default {
  name: "App",
  data() {
    return {
      name: "Minh Hoang",
      greet: "Hello",
      comment: "Binding Text",
      htmlbinding: '<b>Coding</b>',
      headingID: 'heading',
      hack: `<a href="#" onclick="alert('Hello')">Win a prize!</a>"`,
      isDisabled: false,
      status: 'success',
      isPromoted: false,
      isSoldout: true,
      highlightcolor: 'orange',
      headerSize: 50,
      headerStyleObject: {
        color: 'orange',
        fontSize: '50px',
        padding: '20px'
      },
      baseStyleObject: {
        fontSize: '50px',
        padding: '10px'
      },
      successStyleObject: {
        color: 'green',
        backgroundColor: 'lightgreen',
        border: '1px solid green',
        padding: '20px'
      }
    };
  },
};
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="I did it!" />
    </div>
  </header>

  <main>
    <div> {{ greet }} {{ name }}</div>
    <div v-text="comment"></div>
    <div v-html="htmlbinding"></div>
    <div v-html="hack"></div>
    <h2 v-bind:id="headingID">Heading</h2>
    <button v-bind:disabled="isDisabled">Bind</button>
    <h2 class = "underline">Underlined text</h2>
    <h2 class = "underline" v-bind:class="status">Status</h2>
    <h2 v-bind:class="isPromoted && 'promoted'">Promoted movie</h2>
    <h2 v-bind:class="isSoldout ? 'sold-out' : 'new'">Soldout ? movie</h2>
    <h2 v-bind:class="['new', 'promoted']">Newly promoted movie</h2>
    <h2 v-bind:class="[isPromoted && 'promoted', isSoldout ? 'sold-out' : 'new']">Array conditional movie</h2>
    <h2 v-bind:class="{
      promoted:isPromoted,
      new: !isSoldout,
      'sold-out': isSoldout
    }">Object conditional movie</h2>
    <h2 v-bind:style="{
      color: highlightcolor,
      'font-size': headerSize + 'px',
      padding: '20px',
    }">Inline style</h2>
    <h2 v-bind:style="headerStyleObject"> Style Object</h2>
    <div v-bind:style="[baseStyleObject, successStyleObject]"> Success Style</div>"
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
.underline {
  text-decoration: underline;
}
.promoted {
  font-style:italic;
}
.new {
  color: olivedrab;
}
.sold-out{
  color: red;
}
</style>
