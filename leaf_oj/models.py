from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Problem(models.Model):
    # 题目难度级别选项
    DIFFICULTY_CHOICES = [
        ('Easy1', '简单1'),
        ('Easy2', '简单2'),
        ('Easy3', '简单3'),
        ('Easy4', '简单4'),
        ('Easy5', '简单5'),
        ('Medium6', '中等6'),
        ('Medium7', '中等7'),
        ('Medium8', '中等8'),
        ('Medium9', '中等9'),
        ('Medium10', '中等10'),
        ('Hard11', '困难11'),
        ('Hard12', '困难12'),
        ('Hard13', '困难13'),
        ('Hard14', '困难14'),
        ('Hard15', '困难15'),
    ]

    # 核心字段
    problem_id = models.CharField(max_length=20, unique=True, verbose_name='题目编号')
    title = models.CharField(max_length=200, verbose_name='题目标题')
    description = models.TextField(verbose_name='题目描述')
    input_description = models.TextField(verbose_name='输入描述')
    output_description = models.TextField(verbose_name='输出描述')
    sample_input = models.TextField(verbose_name='样例输入')
    sample_output = models.TextField(verbose_name='样例输出')
    time_limit = models.IntegerField(default=1000, verbose_name='时间限制(ms)')  # 单位毫秒
    memory_limit = models.IntegerField(default=256, verbose_name='内存限制(MB)')  # 单位MB
    difficulty = models.CharField(
        max_length=10, 
        choices=DIFFICULTY_CHOICES, 
        default='Medium',
        verbose_name='难度'
    )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'oj_problem'  # 自定义数据库表名

    def __str__(self):
        return self.title

class Submission(models.Model):
    # 判题状态选项
    STATUS_CHOICES = [
        ('Pending', '等待中'),
        ('Running', '运行中'),
        ('Accepted', '通过'),
        ('Wrong Answer', '答案错误'),
        ('Time Limit Exceeded', '超时'),
        ('Memory Limit Exceeded', '内存超限'),
        ('Compile Error', '编译错误'),
    ]

    # 关联字段
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='提交用户')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name='关联题目')
    code = models.TextField(verbose_name='提交代码')
    language = models.CharField(max_length=20, default='C++', verbose_name='编程语言')
    status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default='Pending',
        verbose_name='判题状态'
    )
    run_time = models.IntegerField(null=True, verbose_name='运行时间(ms)')  # 实际耗时
    run_memory = models.IntegerField(null=True, verbose_name='内存占用(KB)')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')

    class Meta:
        db_table = 'oj_submission'
        ordering = ['-submit_time']  # 按提交时间倒序排列

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    solved_count = models.IntegerField(default=0, verbose_name='已解决题目数')
    attempted_count = models.IntegerField(default=0, verbose_name='尝试题目数')
    rating = models.IntegerField(default=1500, verbose_name='用户积分')

    class Meta:
        db_table = 'oj_user_profile'

    def __str__(self):
        return self.user.username

class Contest(models.Model):
    title = models.CharField(max_length=100, verbose_name='竞赛名称')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    problems = models.ManyToManyField(Problem, verbose_name='题目集合')
    participants = models.ManyToManyField(User, blank=True, verbose_name='参赛者')

    class Meta:
        db_table = 'oj_contest'

    def __str__(self):
        return self.title