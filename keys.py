import json as js
"""

"record-declaration": {
      "beginCaptures": {
        "1": {
          "name": ""
        }
      },
      "endCaptures": {
        "1": {
          "name": ""
        }
      },
      "patterns": [
        {
          "include": "#comment"
        },
        {
          "beginCaptures": {
            "1": {
              "name": ""
            }
          },
          "patterns": [
            {
              "beginCaptures": {
                "1": {
                  "name": ""
                }
              },
              "patterns": [
                {
                  "patterns": [
                    {
                      "include": "#declaration"
                    }
                  ]
                },
                {
                  "include": "#expression"
                }
              ]
            },
            {
            },
            {
              "include": "#identifier"
            }
          ]
        },
        {
          "include": "#declaration"
        }
      ]
    },

"""


def main():
    data = js.load(open('syntaxes/fore.tmLanguage.json'), )
    print(list(data.keys()))

    print(js.dumps({i:rec(data['repository'][i], 'patterns') for i in data['repository']}, indent=2))
    print(js.dumps(rec(data, 'patterns'), indent=2))
    return
    a={}
    for i in data['repository']:
        print(i)
        a_i_content = [j.get('include', '') for j in data['repository'][i]['patterns'] if j.get('include')!=None]
        a[i]=[j.get('include', '').replace('#','') for j in data['repository'][i]['patterns'] if j.get('include')!=None]
    print(js.dumps(a, indent=2))
    res=[]
    # for i in a:
    #     res.append(('repo', i))
    for i in a:
        for j in a[i]+[]:
            
            res.append((i,j))
    return res

def rec(a:dict, key):
    res=[]
    if key=='include':
        return a.get('include')
    for i in a.get(key, []):
        if i.get('include') is not None:
            res.append(rec(i, 'include'))
        if i.get('patterns') is not None:
            rec_returned = rec(i, 'patterns')
            for j in rec_returned+[]:
                res.append(j)
        
    return res



if __name__ == '__main__':
    main()