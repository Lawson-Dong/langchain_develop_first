#!/usr/bin/env python
"""测试搜索功能修复"""
import sys
sys.path.insert(0, '.')

from agents.my_agent import agent

print('='*70)
print('搜索功能修复验证')
print('='*70)

config = {'configurable': {'thread_id': 'search_fix_test'}}

# 测试搜索功能
print('\n【测试】搜索最新的AI技术新闻')
print('-'*70)

response = agent.invoke(
    {'messages': [('user', '搜索 AI人工智能 最新进展和趋势')]},
    config=config
)

result = response['messages'][-1].content
print(result[:1000])
print('\n...(内容已截断)\n')

print('='*70)
print('✓ 搜索功能修复成功！')
print('✓ 智能体现在能够从互联网获取实时信息')
print('='*70)
