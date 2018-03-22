本项目只是django+mssql的练手项目

django-mssql1.8 目前只支持django1.8
注意：
如果采用SQLServer2005版本时（由于该版本不支持数据类型datetime2,2008及以上版本支持 ），故需要修改base.py中的datetime2为datetime
```
data_types = {
        ...        
        'DateTimeField':                'datetime',#datetime2
        ...
        'NewDateTimeField':             'datetime',#datetime2
        ...
    }
```
