children=`ps -ef|grep uwsgi|grep -v grep|awk '{print $2}'`
parents=`ps -ef|grep uwsgi|grep -v grep|awk '{print $3}'`

for child in $children
do
    
  if [[ "${parents[*]@/$child/}" != "${parents[*]}" ]]
  then
       pid=$child
       
       echo '更新代码'
       cd demo && git pull origin master
 
       echo '重启uwsgi'
       kill -HUP $pid
       
       echo '删除pyc'
       rm -f `find . -name *pyc`
       
       echo '重启爬虫'
       supervisorctl restart youku
       
        
       
  fi
done



echo 'success'
