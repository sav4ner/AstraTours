<template>
  <div class="hello">

    <!-- nav menu -->
    <div class="sticky" style="width:100%;">
      <nav class="navbar1">
        <img :src="require('./assets/logo.png')" alt="Sav4ner" class="logo"> <h1 class="he">Astra<span>Tours</span></h1>
        <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
        <ul class="">
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'home'}"><i class="fa fa-home" aria-hidden="true"></i>
Home</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'destinations'}"><i class="fa fa-plane" aria-hidden="true"></i> Destinations</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'hotels'}"><i class="fa fa-bed" aria-hidden="true"></i> Hotels</router-link>
            </li>
            <li class="nav-item">
               
                <router-link class="nav-link1" :to="{name : 'bookings'}"><i class="fa fa-bookmark-o" aria-hidden="true"></i> Bookings</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'cart'}"><i class="fa fa-shopping-cart" aria-hidden="true"></i> Cart</router-link>
            </li>
            <li class="nav-item" id="image">
                
                <router-link class="nav-link1" :to="{name : 'cart'}"> </router-link>
            </li>
        </ul>
        
      </nav>
    </div>
   
    
  </div>
</template>

<script>
export default {
  name: 'navigation',
  props: {
    msg: String
  }
}

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

body{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

}
.he{
  color: aliceblue;
  float: left;
  margin-top: 15px;
  font: bolder;
  font-family: 'Comforter', cursive;
  font-family: 'Dancing Script', cursive;
  font-family: 'Tillana', cursive;
}
.he span{
  color: orange;
}
/* nav decorators */
 .router-link-exact-active router-link-active {
    background: #454647;
    transition: .5s;
    color: antiquewhite;
    padding:14px 10px;
    border-radius: 4px;
  }
  .nav-link1:hover{
    background: #454647;
    /* transition: .01s; */
    color: aliceblue;
    /* padding:17px 10px; */
    border-radius: 4px;
    margin-top: 4px;
  }
a{
  text-decoration: none;
}
.navbar1{
  margin-top: 0;
  width:100%;
  height: 65px;
  background: #16161d;
  position: absolute;
  
  
}
.navbar1 ul {
  list-style: none;
  display: flex;
  flex-direction: row;
  float: right;
  margin-right: 10%;
  margin-top:-1px;
  
  
}
.nav-item {
    margin-top: 2px;
   padding: 0 1.6vh;
}
.nav-link1{
  /* margin-top: 10px; */
  color:orange;
  font:bolder;
  font-size: 20px;
   padding: 12px 8px;
}
.sticky{
    position: fixed;
    z-index:2;
}
.logo{
  margin: 2px 5px;
  height: 60px;
  width: auto;
  float: left;
  margin-top: 22px;
  margin-left: 3%;
}
#image{
  float: right;
  color: orange;
  font: bolder;
  margin-right: -3%;

}
</style>
