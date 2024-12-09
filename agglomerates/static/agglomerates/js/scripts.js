function hide_show_table(col_name)
{
    var checkbox_val=document.getElementById(col_name).value;
    if(checkbox_val=="hide")
    {
        var all_col=document.getElementsByClassName(col_name);
      
        for(var i=0;i<all_col.length;i++)
        {
           
                all_col[i].style.display="none";
          
          
            
        }
      
            document.getElementById(col_name+"_head").style.display="none";
            document.getElementById(col_name).value="show";
        
            
    }   
    else
    {
        var all_col=document.getElementsByClassName(col_name);
        for(var i=0;i<all_col.length;i++)
        {
            all_col[i].style.display="table-cell";
        }
       
        document.getElementById(col_name+"_head").style.display="table-cell";
        document.getElementById(col_name).value="hide";
    }
}
function hide_id(col_name)
{
    var checkbox_val=document.getElementById(col_name).value;
    
    if(checkbox_val=="hide")
    {
        var col=document.getElementsByClassName(col_name);
        
        for(var i=0;i<col.length;i++)
        {
            console.log(col[i].getAttribute("class"))
            if(col[i].getAttribute("class")=="entry_output_id"){
              
                col[i].style.visibility="hidden";
              
            
            }
            document.getElementById(col_name+"_head").style.visibility="hidden";           
        }       
    
    }
}
function scroll(ev){
    if(window.pageYOffset>50)alert('User has scrolled at least 400 px!');
}

document.addEventListener('DOMContentLoaded', function() {
    const item_menu_active = window.localStorage.getItem('active_menu')
    // alert(item_menu_active)
    const menu=document.querySelector('.menu');
    for(i=0; i<menu.childNodes.length; i++){
        if(menu.childNodes[i].href==item_menu_active){
            menu.childNodes[i].classList.add('active');
            // alert(menu.childNodes[i].href);
        }else{
            // menu.childNodes[i].classList.remove('active');
        }
    } 
    // menu.childNodes.forEach(item => {
    // console.log(item.getAttribute('href'))
    // });
    menu.addEventListener('click', e => {
      const target = e.target;
      window.localStorage.setItem('active_menu', e.target);  
  })
    const tbody = document.querySelector('#table_agglomerates tbody');
    if(tbody){
        tbody.addEventListener('click', function (e) {
            const cell = e.target.closest('td');
            if (!cell) {return;} // Quit, not clicked on a cell
            const row = cell.parentElement;
            if(cell.cellIndex==21){
              var ids=
               console.log(row.getElementsByClassName('entry_output_id')[0].innerHTML);
               
            }
           
          });
    }
    const form_edit_actual=document.querySelectorAll('.edit_actual_output p');
    console.log(form_edit_actual);
    for (var i=0; i<form_edit_actual.length-1;  i++) {
        if(i>-1 ){
            form_edit_actual[i].style.display='none';
        }
    }
    var show_hide_column_control=document.getElementById('show_hide_column_control');
    if(show_hide_column_control){
        show_hide_column_control.onclick = function(event){       
        document.getElementById("crossing").classList.toggle("expand");
        if (event.target.classList.contains('collapse')) {
            document.getElementById("show_hide_column_control").classList.remove('collapse');
            document.getElementById("show_hide_column_control").classList.add('deploy');
        }else{
            document.getElementById("show_hide_column_control").classList.remove('deploy');
            document.getElementById("show_hide_column_control").classList.add('collapse');
        }
       
    }


        
      }
      var show_hide_formula_control= document.getElementById('show_hide_formula_control');
      if(show_hide_formula_control){
         show_hide_formula_control.onclick = function(event){       
        document.getElementById("formula").classList.toggle("minimize_formula");
        if (event.target.classList.contains('deploy_formula')) {
            document.getElementById("show_hide_formula_control").classList.remove('deploy_formula');
            document.getElementById("show_hide_formula_control").classList.add('collapse_formula');
        }else{
            document.getElementById("show_hide_formula_control").classList.remove('collapse_formula');
            document.getElementById("show_hide_formula_control").classList.add('deploy_formula');
        }
      }
       
       

        
      }
      let startFunctionPos = 300;
      let isActiveFun = false;
      window.addEventListener('scroll', () => {
      if(!isActiveFun && window.pageYOffset > startFunctionPos ){
       document.getElementById("menu").classList.add('fixed');
      isActiveFun  = !isActiveFun;
      }else if(window.pageYOffset <= startFunctionPos){
        document.getElementById("menu").classList.remove('fixed');
        isActiveFun = false;
      }
      })
      


  }); 

