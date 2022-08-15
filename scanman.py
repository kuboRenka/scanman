#!/usr/bin/python3

from email.policy import default
import click
from scanman.core import Prime, ScannerType, TableType


@click.command()
@click.option('-b', '--html_path', required=True, help="漏扫报告html文件夹路径")
@click.option('-t', '--table_type', default="DJCP", type=click.Choice(["YPG", "DJCP"]), show_default=True, help="选择云评估格式或等级测评格式导出")
@click.option('-s', '--scanner_type', default="RSAS", type=click.Choice(["RSAS"]), show_default=True, help="所使用的漏洞扫描器类型")
@click.option('-x', '--xlsx_path', default='', help='漏扫目标信息的Excel表路径，表头必须包含ip和name字段')
@click.option('-o', '--output_path', default='./out.docx', help='Word格式报告输出全路径')
@click.option('-r', '--recursive/--no-recursive',  default=False, show_default=True, help="从html文件夹路径下递归地读取命名符合ip.html的文件")
def cli(html_path, xlsx_path, output_path, table_type, scanner_type, recursive):
  prime = Prime()
  prime.set_html_path(html_path)
  prime.set_xlsx_path(xlsx_path)
  prime.set_output_full_path(output_path)
  prime.set_recursive_read(recursive)

  table_type_mapping = {
      "YPG": TableType.YPG,
      "DJCP": TableType.DJCP
  }
  prime.set_table_type(table_type_mapping[table_type])

  scanner_type_mapping = {
      "RSAS": ScannerType.RSAS,
      "TRX": ScannerType.TRX,
      "NESSUS": ScannerType.NESSUS
  }
  prime.set_scanner_type(scanner_type_mapping[scanner_type])

  prime.run()


if __name__ == "__main__":
  cli()
